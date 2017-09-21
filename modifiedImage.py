# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
import numpy as np
from PyQt4.Qt import QBuffer, QIODevice
from PIL import Image, ImageQt
import cStringIO
import matplotlib.pyplot as plt

def fft(data):
    res = np.fft.fft2(data, s=(512,512))
    res = np.fft.fftshift(res)
    newArray = np.log(np.absolute(res))
    minV, maxV = newArray.min(), newArray.max()
    newArray -= minV
    newArray *= 255 / (maxV - minV)
    return newArray.astype(np.uint8)

class ModifiedImage():
    
    def __init__(self, image):
        self.image = image
        self.modifiedImage = None
        self.applyFilter()
    
    def applyFilter(self):
        # Konvertujem QImage do grayscale
        #pil_im = ImageQt.fromqimage(self.image).convert('L')
        
        buffer = QBuffer()
        buffer.open(QIODevice.ReadWrite)
        self.image.save(buffer, "bmp")

        strio = cStringIO.StringIO()
        strio.write(buffer.data())
        buffer.close()
        strio.seek(0)
        pil_im = Image.open(strio).convert('L')
		# Pole v Numpy 8bit oer pixel
        numpyArray = np.array(np.asarray(pil_im), copy=True)
        typeBefore = numpyArray.dtype
        # Tu si urob filter nad polom
        
        #result_array = np.zeros_like(input_image)  # make sure data types, 
        # sizes and numbers of channels of input and output numpy arrays are the save
		
        numpyArray2 = fft(numpyArray)
        #for i in range(500):
        #   numpyArray2[i][i] = 150
		

		
        #print("a", repr(numpyArray2[i][i]))
        print("b", numpyArray2)
        
        
		
        # koniec filtra, konvertujem obrazok nazad to QTimage
        self.modifiedImage = ImageQt.ImageQt(Image.fromarray(numpyArray2, 'L').convert('RGB'))
        
    def get(self):
        return self.modifiedImage
