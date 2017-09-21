# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
from PyQt4.Qt import QMainWindow
import matplotlib.pyplot as plt
import numpy as np

# Local imports
from screenCaptureModifier.UI.mainWindowWidget import Ui_MainWindow
from screenCaptureModifier.imageViewer import ImageViewer
import screenCaptureModifier

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
        screenCaptureModifier.colorMap = self._makeCmap("plasma")

    def setCmapVirdis(self):
        screenCaptureModifier.colorMap = self._makeCmap("viridis")
        
    def setCmapMagma(self):
        screenCaptureModifier.colorMap = self._makeCmap("magma")
        
    def setCmapInferno(self):
        screenCaptureModifier.colorMap = self._makeCmap("inferno")
        
    def setCmapNone(self):
        screenCaptureModifier.colorMap = None
        
    def _makeCmap(self, name):
        inferno = plt.get_cmap(name)
        a = np.array(inferno.colors)
        val = a.reshape(768)
        val *= 255
        return val.astype(np.uint8)