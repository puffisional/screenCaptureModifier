# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
import numpy as np
from PyQt4.Qt import QBuffer, QIODevice
from PIL import Image, ImageQt
import cStringIO
import time
import screenCaptureModifier

def scale_range (input, max):
    input += -(np.min(input))
    aMax = np.max(input)
    if np.max(input) <= 0: aMax = 1
    input /= aMax / max
    return input

def fft(data):
    res = np.fft.fft2(data, s=data.shape)
    res = np.fft.fftshift(res)
    newArray = np.log(np.absolute(res))
    newArray = scale_range(newArray, 255)
    return newArray.astype(np.uint8)

class ModifiedImage():
    
    def __init__(self, image):
        self.image = image
        self.modifiedImage = None
        self.applyFilter()
    
    def applyFilter(self):
        # Konvertujem QImage do grayscale
        
        imgBuffer = QBuffer()
        imgBuffer.open(QIODevice.ReadWrite)
        self.image.save(imgBuffer, "bmp")

        strio = cStringIO.StringIO()
        strio.write(imgBuffer.data())
        imgBuffer.close()
        strio.seek(0)
        pil_im = Image.open(strio).convert('L')
        
        # Pole v Numpy 8bit oer pixel
        numpyArray = np.asarray(pil_im)
        # Tu si urob filter nad polom
        
        numpyArray = fft(numpyArray)
        
        # koniec filtra, konvertujem obrazok nazad to QTimage
        pilOutput = Image.fromarray(numpyArray, 'L')
        
        if screenCaptureModifier.colorMap is not None:
            pilOutput.putpalette(screenCaptureModifier.colorMap)
            
        self.modifiedImage = ImageQt.ImageQt(pilOutput.convert('RGB'))
        
    def get(self):
        return self.modifiedImage
