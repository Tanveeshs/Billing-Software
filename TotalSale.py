# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/TotalSaleLhlGga.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import pymongo


myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']
mycol = mydb['Invoice']


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 80, 81, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 70, 67, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 150, 67, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Bills Made:"))
        self.label_2.setText(_translate("Dialog", "Total Sale:"))
        self.onGenBills()

    def onGenBills(self):
        date = datetime.datetime.today().date()
        mydoc = mycol.find()
        sale=0
        bills=0
        for inst in mydoc:
            if inst['Date'] == str(date):
                sale += int(inst['TotalAmount'])
                bills += 1
        self.label_3.setText(str(bills))
        self.label_4.setText(str(sale))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

