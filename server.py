# -*- coding: utf-8 -*-

# Global imports
from __future__ import print_function
import sys
from PyQt4.QtGui import QApplication

# Local imports
from screenCaptureModifier import mainWindow
from screenCaptureModifier.screenCapture import ScreenCapture
from PyQt4.Qt import QRect, SIGNAL, QImage
import zmq
from threading import Thread
from time import sleep
import numpy as np
import signal
import argparse
import zlib
import json
import Queue

class zmqPublisher():
    
    zmqServerSocket = None
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.zmqPendingMessages = Queue.deque()
        self.start()
    
    def start(self):
            '''
            Intitate zmq server.
            Start server listening thread afterwards.
            @param host: String
            @param port: Int
            '''
            try:
                self.context = zmq.Context()  # Get zmq context
                self.socket = self.context.socket(zmq.PUB)  # Initiate publisher socket
                self.socket.setsockopt(zmq.LINGER, 0)  # Discard all pending message after client disconnect
                self.socket.bind("tcp://%s:%i" % (self.host, self.port))  # Bind to the ZmqPublisher default port
                self.connected = True
                Thread(target=self._mainThread).start()
            except Exception, e:
                print(e)
        
    def _mainThread(self):
        while self.connected:
            while len(self.zmqPendingMessages) > 0:
                topic, image = self.zmqPendingMessages.popleft()
                image = image.convertToFormat(QImage.Format_RGB888)
                ptr = image.bits()

                ptr.setsize(image.byteCount())
                numpyData = zlib.compress(np.asarray(ptr, dtype=np.ubyte).tostring(), 4)
                width, height = image.width(), image.height()
                self.socket.send_multipart(["%s_%i_%i" %  (topic, width, height), numpyData])
            sleep(0.005)
    
    def send(self, topic, image):
        self.zmqPendingMessages.append([topic, image])
        
    def close(self, release=False):
        self.zmqPendingMessages.clear()
        self.connected = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    p = argparse.ArgumentParser()
    p.add_argument("--zmqHost", default="127.0.0.1")
    p.add_argument("--zmqPort", default=8889)
    p.add_argument("--coords", default="0,0,1920,1080")
    p.add_argument("--fps", default=5)
    args = p.parse_args()
    
    window = mainWindow.MainWindow()
    window.setWindowTitle("Server version of viewer")
    window.show()
    
    # Tu si vyberas coordinaty na grabovanie plochy a fps
    x,y,width,height = args.coords.split(",")
    capture = ScreenCapture(coords=QRect(int(x), int(y), int(width), int(height)), fps=int(args.fps))
    
    server = zmqPublisher(args.zmqHost, args.zmqPort)
    
    def sendOriginalPicture(frameBuffer):
        server.send(b"original", frameBuffer[-1].copy())
        
    def sendModifiedPicture(frameBuffer):
        server.send(b"modified", frameBuffer[-1].copy())
    
    def onClose():
        capture.newScreen.disconnect(sendOriginalPicture)
        capture.newTransformedScreen.disconnect(sendModifiedPicture)
        server.close()
    
    capture.newScreen.connect(sendOriginalPicture)
    capture.newTransformedScreen.connect(sendModifiedPicture)
    
    capture.newScreen.connect(window.originalPictureWidget.updateImage)
    capture.newTransformedScreen.connect(window.transofrmedPictureWidget.updateImage)
    
    window.onCloseAccept = onClose
    
    app.connect(app, SIGNAL("aboutToQuit()"), window.onCloseAccept)
    signal.signal(signal.SIGINT, lambda *args, **kwargs: window.close())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    app.exec_()
