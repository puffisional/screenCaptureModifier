# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
import sys
from PyQt4.QtGui import QApplication

# Local imports
from screenCaptureModifier import mainWindow
from screenCaptureModifier.screenCapture import ScreenCapture
from PyQt4.Qt import QRect

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = mainWindow.MainWindow()
    window.show()
    
    capture = ScreenCapture(coords=QRect(0,0,1500,1000), fps=32)
    
    capture.newScreen.connect(window.originalPictureWidget.updateImage)
    capture.newTransformedScreen.connect(window.transofrmedPictureWidget.updateImage)
    
    app.exec_()