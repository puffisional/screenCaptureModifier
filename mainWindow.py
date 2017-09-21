# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
from PyQt4.Qt import QMainWindow
import numpy as np

# Local imports
from screenCaptureModifier.UI.mainWindowWidget import Ui_MainWindow
from screenCaptureModifier.imageViewer import ImageViewer
import screenCaptureModifier
from screenCaptureModifier.colorMaps import cmapVirdis, cmapInferno, cmapPlasma, cmapMagma

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
        
    def setCmapPlasma(self):
        screenCaptureModifier.colorMap = cmapPlasma

    def setCmapVirdis(self):
        screenCaptureModifier.colorMap = cmapVirdis
        
    def setCmapMagma(self):
        screenCaptureModifier.colorMap = cmapMagma
        
    def setCmapInferno(self):
        screenCaptureModifier.colorMap = cmapInferno
        
    def setCmapNone(self):
        screenCaptureModifier.colorMap = None