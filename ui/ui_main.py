from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_map_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_map_1.setMinimumSize(QtCore.QSize(435, 153))
        self.label_map_1.setMaximumSize(QtCore.QSize(435, 153))
        self.label_map_1.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_map_1.setObjectName("label_map_1")
        self.horizontalLayout.addWidget(self.label_map_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.label_map_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_map_2.setMinimumSize(QtCore.QSize(480, 267))
        self.label_map_2.setMaximumSize(QtCore.QSize(480, 267))
        self.label_map_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_map_2.setObjectName("label_map_2")
        self.verticalLayout_4.addWidget(self.label_map_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_origion_code = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_origion_code.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.textEdit_origion_code.setObjectName("textEdit_origion_code")
        self.verticalLayout_2.addWidget(self.textEdit_origion_code)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_morse_code = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_morse_code.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.textEdit_morse_code.setObjectName("textEdit_morse_code")
        self.verticalLayout_3.addWidget(self.textEdit_morse_code)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label.raise_()
        self.groupBox_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Morse Code Generator"))
        self.label_map_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_map_2.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Your Code:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Morse Code:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
