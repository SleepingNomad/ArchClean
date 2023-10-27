import os
from shlex import split
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from typing import List
import pickle

def add(lineEdit: QLineEdit, listWidget: QListWidget, path: str) -> None:
    """
    Add the text from the line edit to the list widget and save the items to a file.

    Args:
        lineEdit (QLineEdit): The input line edit widget.
        listWidget (QListWidget): The list widget to add the item to.
        path (str): The path to the file to save the items.

    Returns:
        None: This function does not return anything.
    """
    text: str = lineEdit.text()
    if text:
        item: QListWidgetItem = QListWidgetItem(text)
        listWidget.addItem(item)
        lineEdit.clear()

        items: List[str] = [listWidget.item(i).text() for i in range(listWidget.count())]
        with open(path, 'wb') as file:
            pickle.dump(items, file)
