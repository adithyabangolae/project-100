class Atm(object):
    
    def __init__(self,cashWithdrawl,name,typeOfCard):
        self.cashWithdrawl= cashWithdrawl
        self.name = name
        self.typeOfCard= typeOfCard
        

    def atm(self):
        print("ATM:")


atm1 = Atm("50","Adithya","credit card")
print(atm1.atm())    
print(atm1.cashWithdrawl)
print(atm1.name)
print(atm1.typeOfCard)
   





