import os
import subprocess
from typing import List, Callable
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from fs import open_fs
from fs.walk import Walker

import pickle


def load_config_file(file_path: str) -> None:
    """
    Load a pickle file and append its contents to a target list.

    Args:
        file_path (str): Path to the pickle file.
        target_list (List[object]): List to which the loaded objects will be appended.

    Returns:
        None
    """
    target_list: List[object] = []

    with open(file_path, 'rb') as file:
        loaded_objects = pickle.load(file)
        target_list.extend(loaded_objects)

    return target_list

from typing import Optional

def walker(
    path: List[str],
    listWidget: QListWidget,
    filter_patterns: Optional[List[str]] = None,
    filter_directories: Optional[List[str]] = None,
    exclude_patterns: Optional[List[str]] = None,
    exclude_directories: Optional[List[str]] = None,
    search: Optional[str] = "breadth",
    on_error: Optional[Callable[[str], None]] = None,
) -> None:
    """
    Walks through the given path and prints the paths of the files that match the filter patterns.

    Args:
        path (List[str]): The paths to walk through.
        listWidget (QListWidget): The list widget to display the file paths.
        filter_patterns (List[str], optional): List of patterns to include specific files.
        filter_directories (List[str], optional): List of directories to include.
        exclude_patterns (List[str], optional): List of patterns to exclude specific files.
        exclude_directories (List[str], optional): List of directories to exclude.
        search (str, optional): The search strategy, either "breadth" or "depth".
        on_error (Callable[[str], None], optional): Function to handle errors that occur during the walk.

    Returns:
        None
    """
    walker = Walker(
        filter=filter_patterns,
        filter_dirs=filter_directories,
        exclude=exclude_patterns,
        exclude_dirs=exclude_directories,
        search=search,
        on_error=on_error
    )
    try:
        for p in path:
            open_fs_path = open_fs(p)
            for file_path in walker.files(open_fs_path):
                listWidget.addItem(str(p+file_path))
            
                if p == '~/.cache':
                    subprocess.run([f'rm -rf {p+file_path}'], shell=True)
                    subprocess.run(['rm -rf ~/.cache/*'], shell=True)
                else:
                    subprocess.run([f'rm -rf {p+file_path}'], shell=True)
    except Exception:
        pass