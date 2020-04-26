# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/PaytmujnxyI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddBillToDb import addToDb

class Ui_Dialog(object):
    def setupUi(self, Dialog,billed,invNo,netAmt):
        Dialog.setObjectName("Dialog")
        Dialog.resize(585, 288)
        self.Dialog = Dialog
        self.billed = billed
        self.invNo = invNo
        self.netAmt = netAmt
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(46, 16, 111, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 391, 91))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 230, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 221, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Paytm Payment"))
        self.label.setText(_translate("Dialog", "Mobile Number"))
        self.label_2.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Print Bill"))
        self.pushButton.clicked.connect(self.onPrint)

    def onPrint(self):
        print(len(self.lineEdit.text()))
        if len(self.lineEdit.text()) != 10:
            self.label_2.setText('Enter a 10 digit mobile Number')
        elif not self.lineEdit.text().isdigit():
            self.label_2.setText('Enter a numeric number')
        else:
            addB = addToDb(self.invNo,self.billed,self.netAmt,'Paytm',self.netAmt)
            addB.pushToDB()
            self.Dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

