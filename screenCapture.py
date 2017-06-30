# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
from PyQt4.QtGui import QApplication
from PyQt4.Qt import QPixmap, QTimer, QObject, pyqtSignal, QImage
import numpy as np
import copy

class ScreenCapture(QObject):
    
    newScreen = pyqtSignal("QImage")
    newTransformedScreen = pyqtSignal("QImage")
    currentScreen = None
    modifiedScreen = None
    
    def __init__(self, coords, fps=5):
        QObject.__init__(self)
        self.fps = fps
        self.coords = coords
        
        self.captureClock = QTimer()
        self.captureClock.timeout.connect(self.captureScreen)
        self.captureClock.start(1000/self.fps)
    
    def captureScreen(self):
        screenshot = QPixmap.grabWindow(QApplication.desktop().winId())
        self.currentScreen = screenshot.toImage().copy(self.coords)
        self.newScreen.emit(self.currentScreen)

        self.newTransformedScreen.emit(self.imageFilter(self.currentScreen))
    
    def imageFilter(self, image):
        newImage = image.convertToFormat(QImage.Format_RGB888)
        ptr = newImage.bits()
        ptr.setsize(newImage.byteCount())
        numpyArray = np.asarray(ptr, dtype=np.ubyte)
        
        # Tu si urob filter nad polom
        # Usporiadanie je 1D pole s troma hodnotami RGB 8,8,8
        # Teda width x height x 3 [R,G,B,R,G,B,...]
        numpyArray = numpyArray - 15
        
        # koniec filtra
        self.modifiedScreen = QImage(numpyArray.tostring(), newImage.width(), newImage.height(), QImage.Format_RGB888)
        return self.modifiedScreen
