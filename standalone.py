# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
import sys
from PyQt4.QtGui import QApplication

# Local imports
from screenCaptureModifier import mainWindow
from screenCaptureModifier.screenCapture import ScreenCapture
from PyQt4.Qt import QRect
import argparse

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    p = argparse.ArgumentParser()
    p.add_argument("--coords", default="200,200,800,600")
    p.add_argument("--fps", default=15)
    args = p.parse_args()
    
    window = mainWindow.MainWindow()
    window.show()
    
       
    # Tu si vyberas coordinaty na grabovanie plochy a fps
    x,y,width,height = args.coords.split(",")
    capture = ScreenCapture(coords=QRect(int(x), int(y), int(width), int(height)), fps=int(args.fps))
    
    capture.newScreen.connect(window.originalPictureWidget.updateImage)
    capture.newTransformedScreen.connect(window.transofrmedPictureWidget.updateImage)
    
    app.exec_()