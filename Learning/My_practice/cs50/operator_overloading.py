#where we can implement our own  operators using comman symbols like plus ,minus e.t.c
# 

class Vault:
    #this is to contain all money 
    def __init__(self,shillings =0, dollars =0,dinar = 0):
        self.shillings = shillings
        self.dollars = dollars
        self.dinar = dinar

    def __str__(self):
        return f"You have {self.dollars} dollars, {self.dinar} Kuwait dinars and {self.shillings} shillings"

    def __add__(self,other): #by convention the second argument is called other 
        shillings = self.shillings + other.shillings
        dollars = self.dollars + other.dollars
        dinars = self.dinar + other.dinar

        return Vault(shillings,dollars,dinars) #returning an instance with both the totals 

potter = Vault(4000,3000,89000)
print(potter)
weasley = Vault(6000,2000,9000)
print(weasley)

"""adding the contents of two vaults the old fashioned way """

# tot_shillings = potter.shillings + weasley.shillings
# tot_dollars = potter.dollars + weasley.dollars
# tot_dinars = potter.dinar + weasley.dinar

# total = Vault(tot_shillings,tot_dollars,tot_dinars)

"using operator overloading and dander method add in the class ."
#we have overloaded the + operator to add two objects together lol
total = potter + weasley
print(total)









































