#-*- coding: utf-8 -*-

import clr

clr.AddReference("xiApi.NETX64.dll")
clr.AddReference("System.Drawing")

import System.Drawing
from System.Drawing.Imaging import PixelFormat

from xiApi.NET import *


cam = xiCam()
cam.OpenDevice(0)
cam.SetParam(PRM.BUFFER_POLICY, BUFF_POLICY.SAFE)
cam.SetParam(PRM.EXPOSURE, 9000)
cam.SetParam(PRM.GAIN, 10.0)
cam.SetParam(PRM.IMAGE_DATA_FORMAT, IMG_FORMAT.MONO8)

fileobj = System.Drawing.Bitmap(1936, 1216, PixelFormat.Format8bppIndexed)
cam.StartAcquisition()
cam.GetImage(fileobj, 1000)
fileobj.Save("a.bmp")
cam.StopAcquisition()

cam.CloseDevice()
