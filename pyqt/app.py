# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_xCapture(object):
    def setupUi(self, xCapture):
        xCapture.setObjectName("xCapture")
        xCapture.resize(746, 610)
        self.centralwidget = QtWidgets.QWidget(xCapture)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.previewWidget = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewWidget.sizePolicy().hasHeightForWidth())
        self.previewWidget.setSizePolicy(sizePolicy)
        self.previewWidget.setMaximumSize(QtCore.QSize(1936, 1216))
        self.previewWidget.setObjectName("previewWidget")
        self.gridLayout.addWidget(self.previewWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exposureLabel = QtWidgets.QLabel(self.centralwidget)
        self.exposureLabel.setObjectName("exposureLabel")
        self.horizontalLayout.addWidget(self.exposureLabel)
        self.exposureValue = QtWidgets.QLabel(self.centralwidget)
        self.exposureValue.setObjectName("exposureValue")
        self.horizontalLayout.addWidget(self.exposureValue)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.exposureSlider = QtWidgets.QSlider(self.centralwidget)
        self.exposureSlider.setMinimum(1)
        self.exposureSlider.setMaximum(200000)
        self.exposureSlider.setOrientation(QtCore.Qt.Horizontal)
        self.exposureSlider.setObjectName("exposureSlider")
        self.verticalLayout.addWidget(self.exposureSlider)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gainLabel = QtWidgets.QLabel(self.centralwidget)
        self.gainLabel.setObjectName("gainLabel")
        self.horizontalLayout_2.addWidget(self.gainLabel)
        self.gainValue = QtWidgets.QLabel(self.centralwidget)
        self.gainValue.setObjectName("gainValue")
        self.horizontalLayout_2.addWidget(self.gainValue)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gainSlider = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider.setMaximum(100)
        self.gainSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gainSlider.setObjectName("gainSlider")
        self.verticalLayout.addWidget(self.gainSlider)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.captureLabel = QtWidgets.QLabel(self.centralwidget)
        self.captureLabel.setObjectName("captureLabel")
        self.horizontalLayout_3.addWidget(self.captureLabel)
        self.captureValue = QtWidgets.QLabel(self.centralwidget)
        self.captureValue.setObjectName("captureValue")
        self.horizontalLayout_3.addWidget(self.captureValue)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frameCounter = QtWidgets.QSpinBox(self.centralwidget)
        self.frameCounter.setMinimum(1)
        self.frameCounter.setMaximum(2000)
        self.frameCounter.setObjectName("frameCounter")
        self.horizontalLayout_4.addWidget(self.frameCounter)
        self.captureButton = QtWidgets.QPushButton(self.centralwidget)
        self.captureButton.setObjectName("captureButton")
        self.horizontalLayout_4.addWidget(self.captureButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        xCapture.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(xCapture)
        self.statusbar.setObjectName("statusbar")
        xCapture.setStatusBar(self.statusbar)

        self.retranslateUi(xCapture)
        QtCore.QMetaObject.connectSlotsByName(xCapture)

    def retranslateUi(self, xCapture):
        _translate = QtCore.QCoreApplication.translate
        xCapture.setWindowTitle(_translate("xCapture", "xCapture"))
        self.previewWidget.setText(_translate("xCapture", "Preview"))
        self.exposureLabel.setText(_translate("xCapture", "Exposure"))
        self.exposureValue.setText(_translate("xCapture", "-"))
        self.gainLabel.setText(_translate("xCapture", "Gain"))
        self.gainValue.setText(_translate("xCapture", "-"))
        self.captureLabel.setText(_translate("xCapture", "Frame capture"))
        self.captureValue.setText(_translate("xCapture", "-"))
        self.captureButton.setText(_translate("xCapture", "Start"))
