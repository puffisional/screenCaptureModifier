# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
import numpy as np
from PIL import Image, ImageQt

class ModifiedImage():
    
    def __init__(self, image):
        self.image = image
        self.modifiedImage = None
        self.applyFilter()
    
    def applyFilter(self):
        # Konvertujem QImage do grayscale
        pil_im = ImageQt.fromqimage(self.image).convert('L')
        # Pole v Numpy 8bit oer pixel
        numpyArray = np.asarray(pil_im)
        
        # Tu si urob filter nad polom
#         numpyArray = numpyArray - 50
        
        # koniec filtra, konvertujem obrazok nazad to QTimage
        self.modifiedImage = ImageQt.ImageQt(Image.fromarray(numpyArray, 'L').convert('RGB'))
        
    def get(self):
        return self.modifiedImage
