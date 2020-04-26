# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/addItemobGvLy.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']
mycol = mydb['Items']

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 382)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 70, 111, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 70, 191, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 101, 41))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(170, 260, 92, 23))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 320, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 130, 121, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 200, 191, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 330, 261, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Item"))
        self.label.setText(_translate("Dialog", "Item Name"))
        self.label_2.setText(_translate("Dialog", "Item Price"))
        self.label_3.setText(_translate("Dialog", "Manufacurer"))
        self.checkBox.setText(_translate("Dialog", "In Stock"))
        self.pushButton.setText(_translate("Dialog", "Add Item"))
        self.pushButton.clicked.connect(self.onAddItemClick)
        self.label_4.setText(_translate("Dialog", ""))

    def onAddItemClick(self):

        if len(self.lineEdit.text())==0 or len(self.lineEdit_2.text()) == 0:
            self.label_4.setText('Pleas fill all the fields')
        elif not self.lineEdit_2.text().isdigit():
            self.label_4.setText('Prize Should be a number')
        else:
            mydoc = mycol.find()
            items = []
            for i in mydoc:
                items.append(i['name'])
            if self.lineEdit.text() in items:
                self.label_4.setText('Item already exists')
            else:
                x=''
                if self.checkBox.isChecked():
                    x='y'
                else:
                    x='n'
                mydoc = {
                    'name':self.lineEdit.text(),
                    'price':self.lineEdit_2.text(),
                    'manufacturer':self.lineEdit_3.text(),
                    'stock':x
                }
                mycol.insert(mydoc)
                sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

