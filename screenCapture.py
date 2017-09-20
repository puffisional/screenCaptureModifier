# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
from PyQt4.QtGui import QApplication
from PyQt4.Qt import QPixmap, QTimer, QObject, pyqtSignal
import Queue
from modifiedImage import ModifiedImage

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
        screenshot = QPixmap.grabWindow(QApplication.desktop().winId(), self.coords.x(), self.coords.y(), 
                                        self.coords.width(), self.coords.height())
        self.screenBuffer.append(screenshot.toImage().copy())
        self.transformedScreenBuffer.append(ModifiedImage(self.screenBuffer[-1]).get())
        
        self.newScreen.emit(self.screenBuffer)
        self.newTransformedScreen.emit(self.transformedScreenBuffer)