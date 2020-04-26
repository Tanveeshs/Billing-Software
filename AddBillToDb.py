import pymongo
import datetime
myClient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myClient['Billing']

mycol = mydb['Invoice']


class addToDb:

    def __init__(self, number, billed, totalAmt, mode, cashT):
        self.number = number
        self.billed = billed
        self.totalAmt = totalAmt
        self.mode = mode
        self.cashT = cashT

    def pushToDB(self):
        myquery = {
            'InvoiceNumber': self.number,
            'Billed Items': self.billed[1:],
            'TotalAmount': self.totalAmt,
            'ModeOfPayment': self.mode,
            'CashTendered': self.cashT,
            'Date':str(datetime.datetime.today().date())
        }
        mycol.insert(myquery)






