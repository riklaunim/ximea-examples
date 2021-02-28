import abc


class CameraConfiguration:
    @abc.abstractmethod
    def get_instance(self):
        pass

    @abc.abstractmethod
    def min_gain(self):
        pass

    @abc.abstractmethod
    def max_gain(self):
        pass

    @abc.abstractmethod
    def gain_increment(self):
        pass

    @abc.abstractmethod
    def min_exposure(self):
        pass

    @abc.abstractmethod
    def max_exposure(self):
        pass

    @abc.abstractmethod
    def exposure_increment(self):
        pass


class Camera:
    def __init__(self, cam):
        self.cam = cam

    @abc.abstractmethod
    def set_exposure(self, exposure):
        pass

    @abc.abstractmethod
    def set_gain(self, gain):
        pass

    @abc.abstractmethod
    def get_frame(self):
        pass
