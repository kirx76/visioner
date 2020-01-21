# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.InputText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.InputText.setObjectName("InputText")
        self.verticalLayout.addWidget(self.InputText)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Kword = QtWidgets.QLineEdit(self.centralwidget)
        self.Kword.setObjectName("Kword")
        self.verticalLayout.addWidget(self.Kword)
        self.ConvertButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConvertButton.setObjectName("ConvertButton")
        self.verticalLayout.addWidget(self.ConvertButton)
        self.DeconvertButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeconvertButton.setObjectName("DeconvertButton")
        self.verticalLayout.addWidget(self.DeconvertButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.OutputText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.OutputText.setObjectName("OutputText")
        self.verticalLayout.addWidget(self.OutputText)
        self.loadFromFile = QtWidgets.QPushButton(self.centralwidget)
        self.loadFromFile.setObjectName("loadFromFile")
        self.verticalLayout.addWidget(self.loadFromFile)
        self.saveToFile = QtWidgets.QPushButton(self.centralwidget)
        self.saveToFile.setObjectName("saveToFile")
        self.verticalLayout.addWidget(self.saveToFile)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuVis = QtWidgets.QAction(MainWindow)
        self.menuVis.setObjectName("menuVis")
        self.menuCes = QtWidgets.QAction(MainWindow)
        self.menuCes.setObjectName("menuCes")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Начальный текст"))
        self.label_2.setText(_translate("MainWindow", "Ключ-слово"))
        self.ConvertButton.setText(_translate("MainWindow", "Закодировать"))
        self.DeconvertButton.setText(_translate("MainWindow", "Декодировать"))
        self.label_3.setText(_translate("MainWindow", "Зашифрованный текст"))
        self.loadFromFile.setText(_translate("MainWindow", "Загрузить из файла начальный текст"))
        self.saveToFile.setText(_translate("MainWindow", "Сохранить в файл зашифрованный текст"))
        self.menuVis.setText(_translate("MainWindow", "Vigenère"))
        self.menuCes.setText(_translate("MainWindow", "Caesar"))
