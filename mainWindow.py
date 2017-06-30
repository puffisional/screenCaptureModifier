# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
from PyQt4.Qt import QMainWindow

# Local imports
from screenCaptureModifier.UI.mainWindowWidget import Ui_MainWindow
from screenCaptureModifier.imageViewer import ImageViewer

class MainWindow(Ui_MainWindow, QMainWindow):
    
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)

        self.originalPictureWidget = ImageViewer()
        self.transofrmedPictureWidget = ImageViewer()
        
        self.originalPictureFrame.layout().addWidget(self.originalPictureWidget)
        self.transformedPictureFrame.layout().addWidget(self.transofrmedPictureWidget)