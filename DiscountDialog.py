# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/DiscountDialogYtNkJu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets

# import main1

myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']
mycol = mydb['Promotions']


class Ui_Dialog(object):
    percent = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 101, 51))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 191, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 250, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 301, 41))
        self.label_2.setObjectName("label_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Discount Code"))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.label_2.setText(_translate("Dialog", ""))
        self.pushButton.clicked.connect(self.buttonClick)

    def buttonClick(self):
        code = self.lineEdit.text()
        myquery = {'Coupon': code}
        mydoc = mycol.find(myquery)
        try:
            print(mydoc[0]['Coupon'])
            print(mydoc[0]['Redeemed'])
            if mydoc[0]['Redeemed'] == 'N':
                print(1)
                self.percent = mydoc[0]['Percent']
                print(1)
                mycol.update(myquery, {'Coupon': code, 'Redeemed': 'Y'})
                print(1)
                self.label_2.setText('Coupon Code Applied')
            else:
                self.label_2.setText('Coupon code is redeemed')
        except:

            self.label_2.setText("Code not found")




    def getPercent(self):
        return self.percent
