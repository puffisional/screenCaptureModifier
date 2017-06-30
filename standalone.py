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
    
    # Tu si vyberas coordinaty na grabovanie plochy a fps
    capture = ScreenCapture(coords=QRect(0, 0, 800, 600), fps=5)
    
    capture.newScreen.connect(window.originalPictureWidget.updateImage)
    capture.newTransformedScreen.connect(window.transofrmedPictureWidget.updateImage)
    
    app.exec_()