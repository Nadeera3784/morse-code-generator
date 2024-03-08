# -*- coding: utf-8 -*-
RELEASE_MODE = 0
import ui.ui_main
import sys, os, time
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QAction
from PyQt5 import QtGui

# Morse Code
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = ui.ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.move(200, 200)
        self.setWindowTitle("Mose Code v0.2")
        self.sBar = self.statusBar()            

        self.ui.label_map_1.setPixmap(QtGui.QPixmap(r".\assets\number.jpeg"))
        self.ui.label_map_1.setScaledContents(True)
        self.ui.label_map_2.setPixmap(QtGui.QPixmap(r".\assets\character.jpg"))
        self.ui.label_map_2.setScaledContents(True)        

        #====quit action=====
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        self.ui.textEdit_origion_code.textChanged.connect(self.encodeToMorse)      

    def closeEvent(self, event):
        try:
            print("close window:")
        except Exception as e:
            print(e)    
        event.accept()   

    def encodeToMorse(self):
        origion_code = self.ui.textEdit_origion_code.toPlainText()
        '''Morse code encryption'''
        output_str = ''
        input_str = origion_code.upper()
        for i in range(len(input_str)):
            character = input_str[i:i+1]
            if character != ' ' and character != '\n':
                output_str = output_str + " " + CODE[character]
            elif character == '\n':
                output_str = output_str + "\n"
            elif character == ' ':
                output_str = output_str + " "

        self.ui.textEdit_morse_code.clear()
        self.ui.textEdit_morse_code.setText(output_str)



def mycodestart():
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    mycodestart()
