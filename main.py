from json import dumps, loads
from os import path
from sys import exit

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mainwindow import Ui_MainWindow  # импорт нашего сгенерированного файла

tabula_rectaen = 'abcdefghijklmnopqrstuvwxyz'
tabula_rectaru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def err(error):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(error)
    msg.setWindowTitle("Error")
    msg.exec_()


def encrypt(key, text):
    result = []
    space = 0
    if text != '':
        if text[0] in tabula_rectaen:
            tabula_recta = tabula_rectaen
        elif text[0] in tabula_rectaru:
            tabula_recta = tabula_rectaru
        else:
            return False
        for index, ch in enumerate(text):
            if ch != ' ':
                mj = tabula_recta.index(ch)
                kj = tabula_recta.index(key[(index - space) % len(key)])
                cj = (mj + kj) % len(tabula_recta)
                result.append(tabula_recta[cj])
            else:
                space += 1
                result.append(' ')
        return ''.join(result)
    else:
        return False


def decrypt(key, text):
    result = []
    space = 0
    if text != '':
        if text[0] in tabula_rectaen:
            tabula_recta = tabula_rectaen
        elif text[0] in tabula_rectaru:
            tabula_recta = tabula_rectaru
        else:
            return False

        for index, ch in enumerate(text):
            if ch != ' ':
                cj = tabula_recta.index(ch)
                kj = tabula_recta.index(key[(index - space) % len(key)])
                mj = (cj - kj) % len(tabula_recta)
                result.append(tabula_recta[mj])
            else:
                space += 1
                result.append(' ')
        return ''.join(result)
    else:
        return False


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ConvertButton.clicked.connect(self.encryptBtn)
        self.ui.DeconvertButton.clicked.connect(self.decryptBtn)

        self.ui.saveToFile.clicked.connect(self.saveToFile)
        self.ui.loadFromFile.clicked.connect(self.loadFromFile)

    def saveToFile(self):
        out = {
            'line': self.ui.OutputText.toPlainText(),
            'key': self.ui.Kword.text()
        }
        if out['line'] != '':
            file = open('out.json', 'w')
            file.write(dumps(out))
            QMessageBox.about(self, "Success!", "Saving file was successful!")
        else:
            err('Input are clear!')

    def loadFromFile(self):
        self.ui.InputText.clear()
        self.ui.Kword.clear()
        try:
            if path.exists('out.json'):
                inp = open('out.json', 'r')
                line = loads(inp.read())
                self.ui.InputText.insertPlainText(line['line'])
                self.ui.Kword.setText(line['key'])
                QMessageBox.about(self, "Success!", "Loading from file was successful!")
            else:
                err('File does not exist!')
        except:
            err('Check the file!\nSomething went wrong...')

    def encryptBtn(self):
        self.ui.OutputText.clear()
        inputtext = self.ui.InputText.toPlainText().lower()
        keytext = self.ui.Kword.text()
        if keytext != '':
            if not any(map(str.isdigit, inputtext)) and not any(map(str.isdigit, keytext)):
                outtext = encrypt(keytext, inputtext)
                if not outtext:
                    err('Bad value!')
                else:
                    self.ui.OutputText.insertPlainText(outtext)
            else:
                err('Input text have a digits.')
        else:
            err('Keyword is clear!')

    def decryptBtn(self):
        self.ui.OutputText.clear()
        inputtext = self.ui.InputText.toPlainText().lower()
        keytext = self.ui.Kword.text()
        if keytext != '':
            if not any(map(str.isdigit, inputtext)) and not any(map(str.isdigit, keytext)):
                outtext = decrypt(keytext, inputtext)
                if not outtext:
                    err('Bad value!')
                else:
                    self.ui.OutputText.insertPlainText(outtext)
            else:
                err('Input text have a digits.')
        else:
            err('Keyword is clear!')


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

exit(app.exec())
