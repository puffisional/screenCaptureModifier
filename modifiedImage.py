# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
from PyQt4.Qt import QImage
import numpy as np

class ModifiedImage():
    
    def __init__(self, image):
        self.image = image
        self.modifiedImage = None
        self.applyFilter()
    
    def applyFilter(self):
        newImage = self.image.convertToFormat(QImage.Format_RGB888)
        ptr = newImage.bits()
        ptr.setsize(newImage.byteCount())
        numpyArray = np.asarray(ptr, dtype=np.ubyte)
        
        # Tu si urob filter nad polom
        # Usporiadanie je 1D pole s troma hodnotami RGB 8,8,8
        # Teda width x height x 3 [R,G,B,R,G,B,...]
        numpyArray = numpyArray - 50
        
        # koniec filtra
        self.modifiedImage = QImage(numpyArray.tostring(), newImage.width(), newImage.height(), QImage.Format_RGB888)
    
    def get(self):
        return self.modifiedImage