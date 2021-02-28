from unittest import mock

from pyqt import run


class TestPyQtXimeaRecorder:
    @mock.patch('cameras.ximea', mock.MagicMock())
    @mock.patch('run.Recorder._start_preview', mock.MagicMock())
    def test_if_main_window_renders(self, qtbot):
        window = run.Recorder()
        qtbot.addWidget(window)
        assert window.exposureLabel.text() == 'Exposure'
        assert window.gainLabel.text() == 'Gain'
        assert window.captureLabel.text() == 'Frame capture'
