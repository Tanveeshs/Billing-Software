import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']

mycol = mydb['CreditCard']


class addCCtoDB:
    def __init__(self, ccno, name, reciptNo, amount, invNo):
        self.ccno = ccno
        self.name = name
        self.reciptNo = reciptNo
        self.amount = amount
        self.invNo = invNo

    def addToDB(self):
        mydoc = {
            'CardNumber': self.ccno,
            'CardholderName': self.name,
            'ReciptNumber': self.reciptNo,
            'Amount': self.amount,
            'InvoiceNumber': self.invNo
        }
        mycol.insert(mydoc)
