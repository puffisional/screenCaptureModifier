# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowWidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(524, 295)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(6)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame = QtGui.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(250, 250))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelOriginalPicture = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOriginalPicture.sizePolicy().hasHeightForWidth())
        self.labelOriginalPicture.setSizePolicy(sizePolicy)
        self.labelOriginalPicture.setStyleSheet(_fromUtf8("font-weight:bold;background:#f6b442;padding:5"))
        self.labelOriginalPicture.setFrameShape(QtGui.QFrame.Box)
        self.labelOriginalPicture.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelOriginalPicture.setObjectName(_fromUtf8("labelOriginalPicture"))
        self.gridLayout.addWidget(self.labelOriginalPicture, 0, 0, 1, 1)
        self.originalPictureFrame = QtGui.QFrame(self.frame)
        self.originalPictureFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.originalPictureFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.originalPictureFrame.setObjectName(_fromUtf8("originalPictureFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.originalPictureFrame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addWidget(self.originalPictureFrame, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelTransformedPicture = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTransformedPicture.sizePolicy().hasHeightForWidth())
        self.labelTransformedPicture.setSizePolicy(sizePolicy)
        self.labelTransformedPicture.setStyleSheet(_fromUtf8("font-weight:bold;background:#f6b442;padding:5"))
        self.labelTransformedPicture.setFrameShape(QtGui.QFrame.Box)
        self.labelTransformedPicture.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelTransformedPicture.setObjectName(_fromUtf8("labelTransformedPicture"))
        self.gridLayout_2.addWidget(self.labelTransformedPicture, 0, 0, 1, 1)
        self.transformedPictureFrame = QtGui.QFrame(self.frame_2)
        self.transformedPictureFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.transformedPictureFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.transformedPictureFrame.setObjectName(_fromUtf8("transformedPictureFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.transformedPictureFrame)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2.addWidget(self.transformedPictureFrame, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuApplication = QtGui.QMenu(self.menubar)
        self.menuApplication.setObjectName(_fromUtf8("menuApplication"))
        MainWindow.setMenuBar(self.menubar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionOriginal_picture = QtGui.QAction(MainWindow)
        self.actionOriginal_picture.setObjectName(_fromUtf8("actionOriginal_picture"))
        self.actionTransformed_picture = QtGui.QAction(MainWindow)
        self.actionTransformed_picture.setObjectName(_fromUtf8("actionTransformed_picture"))
        self.menuApplication.addAction(self.actionClose)
        self.menubar.addAction(self.menuApplication.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Picture transformation", None))
        self.labelOriginalPicture.setText(_translate("MainWindow", "Original picture", None))
        self.labelTransformedPicture.setText(_translate("MainWindow", "Transformed picture", None))
        self.menuApplication.setTitle(_translate("MainWindow", "Application", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionOriginal_picture.setText(_translate("MainWindow", "Original picture", None))
        self.actionTransformed_picture.setText(_translate("MainWindow", "Transformed picture", None))
