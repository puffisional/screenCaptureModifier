# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
import sys
from PyQt4.QtGui import QApplication

# Local imports
from screenCaptureModifier import mainWindow
from PyQt4.Qt import SIGNAL, pyqtSignal, QObject, QImage
import zmq
from threading import Thread
from time import sleep
import argparse
import signal
import numpy as np
import zlib

class zmqSubscriber(QObject):
    
    zmqServerSocket = None
    newScreen = pyqtSignal("QImage")
    newTransformedScreen = pyqtSignal("QImage")
    
    def __init__(self, host, port):
        QObject.__init__(self)
        self.host = host
        self.port = port
        self.start()
    
    def start(self):
            '''
            Intitate zmq server.
            Start server listening thread afterwards.
            @param host: String
            @param port: Int
            '''
            try:
                context = zmq.Context()
                self.zmqSubSocket = context.socket(zmq.SUB)
                self.zmqSubSocket.connect("tcp://%s:%i" % (self.host, self.port))
                self.zmqSubSocket.setsockopt(zmq.SUBSCRIBE, b"original")
                self.zmqSubSocket.setsockopt(zmq.SUBSCRIBE, b"modified")
                self.zmqSubSocket.setsockopt(zmq.LINGER, 0)
                self.connected = True
                Thread(target=self._mainThread).start()
            except Exception, e:
                print(e)
        
    def _mainThread(self):
        while self.connected:
            try:
                topic, value = self.zmqSubSocket.recv_multipart(flags=zmq.NOBLOCK)
                imageOrigin, width, height = topic.split("_")
                imageData = np.fromstring(zlib.decompress(value), dtype=np.ubyte)
                
                if imageOrigin == b"original": 
                    self.image1 = QImage(imageData.tostring(), int(width), int(height), QImage.Format_RGB888)
                    self.newScreen.emit(self.image1)
                elif imageOrigin == b"modified": 
                    self.image2 = QImage(imageData.tostring(), int(width), int(height), QImage.Format_RGB888)
                    self.newTransformedScreen.emit(self.image2)
            except zmq.Again:  # No data
                sleep(0.01)
        
    def close(self, release=False):
        self.connected = False
        self.zmqSubSocket.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    p = argparse.ArgumentParser()
    p.add_argument("--zmqHost", default="127.0.0.1")
    p.add_argument("--zmqPort", default=8889)
    args = p.parse_args()
    
    window = mainWindow.MainWindow()
    window.setWindowTitle("Client version of viewer")
    window.show()
    
    subscriber = zmqSubscriber(args.zmqHost, args.zmqPort)
    
    subscriber.newScreen.connect(window.originalPictureWidget.updateImage)
    subscriber.newTransformedScreen.connect(window.transofrmedPictureWidget.updateImage)
    
    def onClose():
        subscriber.close()
    
    window.onCloseAccept = onClose
    
    app.connect(app, SIGNAL("aboutToQuit()"), window.onCloseAccept)
    signal.signal(signal.SIGINT, lambda *args, **kwargs: window.close())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
      
    app.exec_()
