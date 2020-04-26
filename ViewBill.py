# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/ViewBillpUAGpJ.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']
mycol = mydb['Invoice']


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 336)
        self.dialog = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 100, 121, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 220, 311, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 120, 161, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 270, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "VIew Bill"))
        self.label.setText(_translate("Dialog", "Invoice Number:"))
        self.pushButton.setText(_translate("Dialog", "View Bill"))
        self.pushButton.clicked.connect(self.onViewBillClick)
    def onViewBillClick(self):
        myquery = {
            'InvoiceNumber':self.lineEdit.text()
        }
        try:
            mydoc = mycol.find(myquery)
            print(mydoc[0]['Billed Items'])
            self.dialog.close()
        except:
            self.label_2.setText('Bill not found')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

