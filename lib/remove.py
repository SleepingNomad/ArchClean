from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from typing import List
import pickle

def remove(listWidget: QListWidget, path: str) -> None:
    """
    Removes the selected item from the QListWidget and updates the file at the given path.

    Args:
        listWidget (QListWidget): The QListWidget from which to remove the item.
        path (str): The path to the file to be updated.
    """
    selected_item = listWidget.currentItem()
    if selected_item is not None:
        listWidget.takeItem(listWidget.row(selected_item))

        with open(path, 'rb') as file:
            items: List[str] = pickle.load(file)

            items.remove(selected_item.text())

            with open(path, 'wb') as file:
                pickle.dump(items, file)
