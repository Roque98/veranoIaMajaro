# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 231, 191))
        self.label.setStyleSheet("background-image: url(:/cct/Acrobot-v1.PNG);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/c1/images/Acrobot.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 290, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 290, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 80, 231, 191))
        self.label_6.setStyleSheet("background-image: url(:/cct3/MountainCar-v0.PNG);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/c4/images/MountainCar.PNG"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 540, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 540, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 330, 231, 191))
        self.label_8.setStyleSheet("background-image: url(:/cct/Acrobot-v1.PNG);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/c4/images/MountainCar.PNG"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 540, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 540, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(280, 330, 231, 191))
        self.label_11.setStyleSheet("background-image: url(:/cct/Acrobot-v1.PNG);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/c6/images/Pendulum.PNG"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(540, 330, 231, 191))
        self.label_12.setStyleSheet("background-image: url(:/cct6/BipedalWalker-v2.PNG);")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/c3/images/BipedalWalker.PNG"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 560, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 231, 191))
        self.label_4.setStyleSheet("background-image: url(:/cct2/CartPole-v1.PNG);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/c2/images/CartPole.PNG"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 540, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(350, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Acrobot-v1"))
        self.pushButton.setText(_translate("MainWindow", "Abrir entorno"))
        self.pushButton.clicked.connect(self.llamarEntornoMartin)
        self.label_3.setText(_translate("MainWindow", "CartPole-v1"))
        self.pushButton_2.setText(_translate("MainWindow", "Abrir entorno"))
        self.pushButton_2.clicked.connect(self.llamarEntornoMarco)
        self.pushButton_3.setText(_translate("MainWindow", "Abrir entorno"))
        self.pushButton_3.clicked.connect(self.llamarEntornoElvira)
        self.label_5.setText(_translate("MainWindow", "MountainCar-v0"))
        self.label_7.setText(_translate("MainWindow", "MountainCarContinuous-v0"))
        self.pushButton_4.setText(_translate("MainWindow", "Abrir entorno"))
        self.pushButton_5.clicked.connect(self.llamarEntornoValladares)
        self.label_9.setText(_translate("MainWindow", "BipedalWalker"))
        self.label_10.setText(_translate("MainWindow", "Pendulum-v0"))
        self.pushButton_5.setText(_translate("MainWindow", "Abrir entorno"))
        self.pushButton_4.clicked.connect(self.llamarEntornoBalbuena)
        self.pushButton_6.setText(_translate("MainWindow", "Abrir entorno"))
        self.pushButton_6.clicked.connect(self.llamarEntornoRoque)
        self.label_13.setText(_translate("MainWindow", "Menu de entornos"))

    # Acciones de los botones

        
    def llamarEntornoBalbuena(self):
        #self.text.setText(random.choice(self.hello))
        #print(call(["python", "run_gym_enviroment.py", "CartPole-v1", "200"]))
        print(call(["python", "run_gym_enviroment.py", "Pendulum-v0", "200"]))

    def llamarEntornoElvira(self):
        #self.text.setText(random.choice(self.hello))
        #print(call(["python", "run_gym_enviroment.py", "CartPole-v1", "200"]))
        print(call(["python", "run_gym_enviroment.py", "MountainCar-v0", "200"]))

    def llamarEntornoMarco(self):
        #self.text.setText(random.choice(self.hello))
        #print(call(["python", "run_gym_enviroment.py", "CartPole-v1", "200"]))
        print(call(["python", "run_gym_enviroment.py", "CartPole-v1", "200"]))

    def llamarEntornoMartin(self):
        #self.text.setText(random.choice(self.hello))
        #print(call(["python", "run_gym_enviroment.py", "CartPole-v1", "200"]))
        print(call(["python", "run_gym_enviroment.py", "Acrobot-v1", "200"]))

    def llamarEntornoRoque(self):
        #self.text.setText(random.choice(self.hello))
        #print(call(["python", "run_gym_enviroment.py", "CartPole-v1", "200"]))
        print(call(["python", "run_gym_enviroment.py", "BipedalWalker-v3", "200"]))

    def llamarEntornoValladares(self):
        #self.text.setText(random.choice(self.hello))
        #print(call(["python", "run_gym_enviroment.py", "CartPole-v1", "200"]))
        print(call(["python", "run_gym_enviroment.py", "MountainCarContinuous-v0", "200"]))

from resourse import BipedalWalker
from resourse import MountainCarContinuous
from resourse import MountainCar
from resourse import Pendulum
from resourse import acrobot
from resourse import cartPole

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

