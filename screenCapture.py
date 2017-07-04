# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
from PyQt4.QtGui import QApplication
from PyQt4.Qt import QPixmap, QTimer, QObject, pyqtSignal, QImage
import numpy as np
import Queue

class ScreenCapture(QObject):
    
    newScreen = pyqtSignal("PyQt_PyObject")
    newTransformedScreen = pyqtSignal("PyQt_PyObject")
    
    def __init__(self, coords, fps=1):
        QObject.__init__(self)
        self.fps = fps
        self.coords = coords
        
        self.captureClock = QTimer()
        self.captureClock.timeout.connect(self.captureScreen)
        self.captureClock.start(1000 / self.fps)
        
        self.screenBuffer = Queue.deque(maxlen=self.fps*2)
        self.transformedScreenBuffer = Queue.deque(maxlen=self.fps*2)
    
    def captureScreen(self):
        screenshot = QPixmap.grabWindow(QApplication.desktop().winId())
        self.screenBuffer.append(screenshot.toImage().copy(self.coords))
        self.transformedScreenBuffer.append(self.imageFilter(self.screenBuffer[-1]))
        
        self.newScreen.emit(self.screenBuffer)
        self.newTransformedScreen.emit(self.transformedScreenBuffer)
    
    def imageFilter(self, image):
        newImage = image.convertToFormat(QImage.Format_RGB888)
        ptr = newImage.bits()
        ptr.setsize(newImage.byteCount())
        numpyArray = np.asarray(ptr, dtype=np.ubyte)
        
        # Tu si urob filter nad polom
        # Usporiadanie je 1D pole s troma hodnotami RGB 8,8,8
        # Teda width x height x 3 [R,G,B,R,G,B,...]
        numpyArray = numpyArray - 50
        
        # koniec filtra
        self.modifiedScreen = QImage(numpyArray.tostring(), newImage.width(), newImage.height(), QImage.Format_RGB888)
        return self.modifiedScreen
