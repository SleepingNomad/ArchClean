from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from typing import List
import pickle


def load(listWidgets: List[QListWidget], paths: List[str]) -> None:
    """
    Load data from pickle files and populate QListWidgets.

    Args:
        listWidgets (List[QListWidget]): The QListWidgets to populate.
        paths (List[str]): The paths to the pickle files.
    """
    try:
        for i, path in enumerate(paths):
            with open(path, 'rb') as file:
                folders: List[str] = pickle.load(file)
                for folder in folders:
                    item = QListWidgetItem(folder)
                    listWidgets[i].addItem(item)
    except Exception:
        pass
