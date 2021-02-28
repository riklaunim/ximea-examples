import sys


from PIL.ImageQt import ImageQt
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import app as viewer
from cameras import ximea


class RecordingWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)

    frames_to_capture = 0
    camera = None

    def run(self):
        for i in range(self.frames_to_capture):
            image = self.camera.get_frame()
            image.save('frames/%d.bmp' % i)
            self.progress.emit(i + 1)
        self.finished.emit()


class Recorder(QtWidgets.QMainWindow, viewer.Ui_xCapture):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        xiC = ximea.XiCMonoConfig()
        self.camera = ximea.XimeaCamera(xiC.get_instance())

        self._configure_sliders(xiC)
        self._connect_signals()
        self._start_preview()

    def _configure_sliders(self, xiC):
        self.exposureSlider.setMinimum(xiC.min_exposure())
        self.exposureSlider.setMaximum(xiC.max_exposure())
        self.exposureSlider.setSingleStep(xiC.exposure_increment())
        self.gainSlider.setMinimum(xiC.min_gain())
        self.gainSlider.setMaximum(xiC.max_gain())
        self.gainSlider.setSingleStep(xiC.gain_increment())

    def _connect_signals(self):
        self.exposureSlider.sliderMoved.connect(self._exposure_changed)
        self.gainSlider.sliderMoved.connect(self._gain_changed)
        self.frameCounter.valueChanged.connect(self._frame_count_changed)
        self.captureButton.clicked.connect(self._start_capture)

    def _start_preview(self):
        self.preview_timer = QtCore.QTimer()
        self.preview_timer.timeout.connect(self._render_preview)
        self.preview_timer.setInterval(200)
        self.preview_timer.setSingleShot(False)
        self.preview_timer.start()

    def _exposure_changed(self, exposure):
        self.exposureValue.setText(str(exposure))
        self.camera.set_exposure(exposure)

    def _gain_changed(self, gain):
        self.gainValue.setText(str(gain))
        self.camera.set_gain(gain)

    def _frame_count_changed(self, frame_count):
        self.captureValue.setText(str(frame_count))

    def _start_capture(self):
        self.preview_timer.stop()
        task = self._get_recording_task()
        task.start()

    def _get_recording_task(self):
        self.thread = QtCore.QThread()
        self.recorder = RecordingWorker()
        self.recorder.frames_to_capture = self.frameCounter.value()
        self.recorder.camera = self.camera
        self.recorder.moveToThread(self.thread)
        self.thread.started.connect(self.recorder.run)
        self.recorder.finished.connect(self.thread.quit)
        self.recorder.finished.connect(self.recorder.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(
            lambda: self.preview_timer.start()
        )
        self.recorder.progress.connect(
            lambda progress: self.statusbar.showMessage("Captured: %d" % progress)
        )
        return self.thread

    def _render_preview(self):
        raw = self.camera.get_frame()
        pixmap = self._convert_to_pixmap(raw)
        self.previewWidget.setPixmap(pixmap)

    @staticmethod
    def _convert_to_pixmap(pillow_image):
        qim = ImageQt(pillow_image)
        return QtGui.QPixmap.fromImage(qim)


def main():
    app = QApplication(sys.argv)
    recorder = Recorder()
    recorder.show()
    app.exec_()


if __name__ == '__main__':
    main()
