class atm(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
    def CashWithdrawl(self):
        print("Cash Withdrawled")
    def BalanceEnquiry(self):
        print("Balance Enquired")
creditcard = atm(123456, 789123)
print(creditcard.cardnumber)
print(creditcard.pinnumber)