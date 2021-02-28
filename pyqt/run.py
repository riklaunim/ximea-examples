import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import app as viewer


class Recorder(QtWidgets.QMainWindow, viewer.Ui_xCapture):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.exposureSlider.sliderMoved.connect(self._exposure_changed)
        self.gainSlider.sliderMoved.connect(self._gain_changed)
        self.frameCounter.valueChanged.connect(self._frame_count_changed)

    def _exposure_changed(self, exposure):
        self.exposureValue.setText(str(exposure))

    def _gain_changed(self, gain):
        self.gainValue.setText(str(gain))

    def _frame_count_changed(self, frame_count):
        self.captureValue.setText(str(frame_count))


def main():
    app = QApplication(sys.argv)
    recorder = Recorder()
    recorder.show()
    app.exec_()


if __name__ == '__main__':
    main()
