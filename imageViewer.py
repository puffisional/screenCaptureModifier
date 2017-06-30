# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function, division
from PyQt4 import QtOpenGL
from PyQt4.Qt import QWidget, QPainter, pyqtSlot, QPixmap, QRect

class ImageViewer(QtOpenGL.QGLWidget, QWidget):
    
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.currentFrame = None
    
    @pyqtSlot(QPixmap)
    def updateImage(self, imagePixmap):
        self.currentFrame = imagePixmap
        self.update()
        
    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)
        if self.currentFrame is not None:
            imgRect = self.currentFrame.rect()
            ri = imgRect.width() / imgRect.height()
            rs = self.width() / self.height()

            if rs > ri:
                w, h = imgRect.width() * self.height() / imgRect.height(), self.height()
            else:
                w, h = self.width(), imgRect.height() * self.width() / imgRect.width()
                
            painter.drawImage(QRect(0, 0, w, h), self.currentFrame, self.currentFrame.rect())
        return QWidget.paintEvent(self, *args, **kwargs)
