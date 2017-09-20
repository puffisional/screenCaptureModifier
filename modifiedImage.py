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
        imgaeFormat = QImage.Format_RGB32
        newImage = self.image.convertToFormat(imgaeFormat)
        ptr = newImage.bits()
        ptr.setsize(newImage.byteCount())
        numpyArray = np.reshape( np.asarray(ptr, dtype=np.ubyte), (newImage.height(), newImage.width()*4))
        
        # Tu si urob filter nad polom
#         numpyArray = numpyArray - 50
        
        # koniec filtra
        self.modifiedImage = QImage(numpyArray.tostring(), newImage.width(), newImage.height(), imgaeFormat)
    
    def get(self):
        return self.modifiedImage