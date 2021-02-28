import PIL.Image

from ximea import xiapi

from . import interface


class XiCMonoConfig(interface.CameraConfiguration):
    def __init__(self):
        self.cam = xiapi.Camera()

    def get_instance(self):
        self.cam.open_device()
        self.cam.set_imgdataformat('XI_MONO8')
        return self.cam

    def min_gain(self):
        return self.cam.get_gain_minimum()

    def max_gain(self):
        return self.cam.get_gain_maximum()

    def gain_increment(self):
        return self.cam.get_gain_increment()

    def min_exposure(self):
        return self.cam.get_exposure_minimum()

    def max_exposure(self):
        ui_max_microseconds = 100000
        return min([self.cam.get_exposure_maximum(), ui_max_microseconds])

    def exposure_increment(self):
        return self.cam.get_exposure_increment()


class XimeaCamera(interface.Camera):
    def set_exposure(self, exposure):
        self.cam.set_exposure(exposure)

    def set_gain(self, gain):
        self.cam.set_gain(gain)

    def get_frame(self):
        img = xiapi.Image()
        self.cam.start_acquisition()
        self.cam.get_image(img)
        data = img.get_image_data_numpy()
        self.cam.stop_acquisition()
        return PIL.Image.fromarray(data, 'L')
