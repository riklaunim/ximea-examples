from ximea import xiapi
import PIL.Image

# create instance for first connected camera
cam = xiapi.Camera()

# start communication
print('Opening first camera...')
cam.open_device()

# settings
cam.set_imgdataformat('XI_MONO8')
cam.set_exposure(20000)

# create instance of Image to store image data and metadata
img = xiapi.Image()

# start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

# get data and pass them from camera to img
cam.get_image(img)
data = img.get_image_data_numpy()

# stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

# stop communication
cam.close_device()

# save acquired image
print('Saving image...')
img = PIL.Image.fromarray(data, 'L')
img.save('xi_example.bmp')
# img.show()

print('Done.')
