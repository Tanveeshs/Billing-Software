# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/CardPaymentsTmTZL.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddBillToDb import addToDb
from AddCardToDb import addCCtoDB

class Ui_Dialog(object):
    def setupUi(self, Dialog,netAmt,billed,invNo):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 286)
        self.Dialog = Dialog
        self.billed = billed
        self.invNo = invNo
        self.netAmt = netAmt
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 111, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 60, 111, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 171, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 120, 271, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 186, 141, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 180, 171, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(358, 240, 121, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(56, 220, 301, 61))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Card Number"))
        self.label_2.setText(_translate("Dialog", "Card Holders Name"))
        self.label_3.setText(_translate("Dialog", "Recipt Number"))
        self.pushButton.setText(_translate("Dialog", "Print Bill"))
        self.pushButton.clicked.connect(self.onPrint)
        self.label_4.setText(_translate("Dialog", ""))

    def onPrint(self):
        print(len(self.lineEdit.text()))
        if len(self.lineEdit.text()) != 4:
            self.label_4.setText('Enter last 4 digits of card')
        elif len(self.lineEdit_2.text()) == 0:
            self.label_4.setText("Enter Card Holder's name")
        elif len(self.lineEdit_3.text()) == 0:
            self.label_4.setText("Enter recipt number")
        else:
            self.label_4.setText("")
            addB = addToDb(self.invNo,self.billed,self.netAmt,'Card',self.netAmt)
            addB.pushToDB()
            addC = addCCtoDB(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.netAmt,self.invNo)
            addC.addToDB()
            self.Dialog.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

