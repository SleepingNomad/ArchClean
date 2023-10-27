import subprocess, os
from shlex import split
from pathlib import Path
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from bin.mainWindow import Ui_ArchClean
from bin.settings import Ui_Settings

from lib.add import add
from lib.remove import remove
from lib.load import load
from lib.walker import walker, load_config_file

from typing import NoReturn

settings_path = Path(f"/home/{os.getlogin()}/.config/sikclean/settings/")



class ArchClean(QMainWindow, Ui_ArchClean):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_abort.clicked.connect(self.close)
        self.pushButton_settings.clicked.connect(self.open_settings)
        self.pushButton_start.clicked.connect(lambda: self.start_walker())

        if not os.path.exists(Path(f"/home/{os.getlogin()}/.config/sikclean/settings/")):
            self.settings_path.mkdir(parents=True, exist_ok=True)

    def start_walker(self):
        paths = load_config_file(f"{settings_path}/paths.cfg") or None
        filter_patterns = load_config_file(f"{settings_path}/filter_patterns.cfg") or None
        filter_dirs = load_config_file(f"{settings_path}/filter_dirs.cfg") or None
        exclude_patterns = load_config_file(f"{settings_path}/exclude_patterns.cfg") or None
        exclude_dirs = load_config_file(f"{settings_path}/exclude_dirs.cfg") or None

        if paths or filter_patterns or filter_dirs or exclude_patterns or exclude_dirs:
            walker(
                paths if paths else None,
                self.listWidget,
                filter_patterns if filter_patterns else None,
                filter_dirs if filter_dirs else None,
                exclude_patterns if exclude_patterns else None,
                exclude_dirs if exclude_dirs else None,
                "depth",
                None
            )

            cmd = [
                'sudo pacman -Sc --noconfirm',
                'sudo pacman -R --noconfirm $(pacman -Qdtq)',
                'sudo paccache -ruk0',
                'sudo journalctl --vacuum-size=50M',
            ]
            try:    
                for i in cmd:
                    process = subprocess.run(split(i), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    for line in process.stdout.decode("utf-8").split("\n"):
                        self.listWidget.addItem(line)
            except Exception:
                pass
            

    def open_settings(self) -> NoReturn:
        """
        Opens the settings window.

        :return: None
        """
        settings_window = SettingsWindow()
        settings_window.exec()



class SettingsWindow(QDialog, Ui_Settings):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)

        self.pushButton_save.clicked.connect(lambda: self.close())

        load([self.listWidget_path, self.listWidget_filter_patterns, self.listWidget_filter_dirs, self.listWidget_exclude_patterns, self.listWidget_exclude_dirs],
             [f"{settings_path}/paths.cfg", f"{settings_path}/filter_patterns.cfg", f"{settings_path}/filter_dirs.cfg", f"{settings_path}/exclude_patterns.cfg", f"{settings_path}/exclude_dirs.cfg"])
        
        self.add_settings()
        self.remove_settings()


    def add_settings(self):
        self.toolButton_add_path.clicked.connect(lambda: add(self.lineEdit_path, self.listWidget_path, f"{settings_path}/paths.cfg"))
        self.toolButton_add_filter_patterns.clicked.connect(lambda: add(self.lineEdit_filter_patterns, self.listWidget_filter_patterns, f"{settings_path}/filter_patterns.cfg"))
        self.toolButton_add_filter_dirs.clicked.connect(lambda: add(self.lineEdit_filter_dirs, self.listWidget_filter_dirs, f"{settings_path}/filter_dirs.cfg"))
        self.toolButton_add_exclude_patterns.clicked.connect(lambda: add(self.lineEdit_exclude_patterns, self.listWidget_exclude_patterns, f"{settings_path}/exclude_patterns.cfg"))
        self.toolButton_add_exclude_dirs.clicked.connect(lambda: add(self.lineEdit_exclude_dirs, self.listWidget_exclude_dirs, f"{settings_path}/exclude_dirs.cfg"))

    def remove_settings(self):
        self.toolButton_remove_path.clicked.connect(lambda: remove(self.listWidget_path, f"{settings_path}/paths.cfg"))
        self.toolButton_remove_filter_patterns.clicked.connect(lambda: remove(self.listWidget_filter_patterns, f"{settings_path}/filter_patterns.cfg"))
        self.toolButton_remove_filter_dirs.clicked.connect(lambda: remove(self.listWidget_filter_dirs, f"{settings_path}/filter_dirs.cfg"))
        self.toolButton_remove_exclude_patterns.clicked.connect(lambda: remove(self.listWidget_exclude_patterns, f"{settings_path}/exclude_patterns.cfg"))
        self.toolButton_remove_exclude_dirs.clicked.connect(lambda: remove(self.listWidget_exclude_dirs, f"{settings_path}/exclude_dirs.cfg"))
      

if __name__ == "__main__":
    app = QApplication([])
    window = ArchClean()
    window.show()
    app.exec()