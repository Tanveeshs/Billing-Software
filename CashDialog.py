# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/CashCvenEm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AddBillToDb import addToDb

class Ui_Dialog(object):
    def setupUi(self, Dialog,netAmt,billed,invNo):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Dialog = Dialog
        self.billed = billed
        self.invNo = invNo
        self.netAmt = netAmt
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 141, 51))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 171, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('0')
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 170, 67, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 240, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.amt = netAmt
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Cash Tendered"))
        self.label_2.setText(_translate("Dialog", "Please return"))
        self.label_3.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "View Change"))
        self.pushButton.clicked.connect(self.onClickConnect)

    def onClickConnect(self,netAmt):
        if self.pushButton.text()== 'View Change':
            self.label_3.setText(str(int(self.lineEdit.text())-int(self.amt)))
            self.pushButton.setText('Print Bill')
        else:
            addB = addToDb(self.invNo,self.billed,self.netAmt,'Cash',self.lineEdit.text())
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

