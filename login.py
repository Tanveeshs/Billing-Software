import sys
import pymongo

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/untitledEpUzUK.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']
mycol = mydb['Login']

from PyQt5 import QtCore, QtGui, QtWidgets
import main1


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 150, 121, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 160, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 360, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 141, 61))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 220, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 280, 261, 17))
        self.label_3.setObjectName("")
        self.label_3.setStyleSheet('color:red')

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setToolTip('Login')
        self.pushButton.clicked.connect(self.onClick)
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def onClick(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        myquery = {'username': username}
        mydoc = mycol.find(myquery)
        try:
            if mydoc[0]['password'] == password:
                print('successful')
                self.next()
            else:
                self.label_3.setText('Wrong Password ')
        except IndexError:
            self.label_3.setText('Wrong Username')
    def next(self):
        ui = main1.Ui_MainWindow()
        ui.setupUi(MainWindow)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
