import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import app as viewer


class Recorder(QtWidgets.QMainWindow, viewer.Ui_xCapture):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    recorder = Recorder()
    recorder.show()
    app.exec_()


if __name__ == '__main__':
    main()
