from __future__ import print_function
import sys
import Pyro4

# A Shop client.
class client(object):
    def __init__(self, name , cash):
        self.name = name
        self.cash = cash

    def doShopping_deposit_cash(self, Shop):
        print("\n*** %s is doing shopping with %s:"\
              % (self.name, Shop.name()))
        print("Log on")
        Shop.logOn(self.name)
        print("Deposit money %s" %self.cash)
        Shop.deposit(self.name, self.cash)
        print("balance=%.2f" % Shop.balance(self.name))
        print("Deposit money %s" %self.cash)
        Shop.deposit(self.name, 50)
        print("balance=%.2f" % Shop.balance(self.name))
        print("Log out")
        Shop.logOut(self.name)
      
    def doShopping_buying_a_book(self, Shop):
        print("\n*** %s is doing shopping with %s:"\
              % (self.name, Shop.name()))
        print("Log on")
        Shop.logOn(self.name)
        print("Deposit money %s" %self.cash)
        Shop.deposit(self.name, self.cash)
        print("balance=%.2f" % Shop.balance(self.name))
        print ("%s is buying a book for %s$"\
               %(self.name,37))
        Shop.buy(self.name,37)
        print("Log out")
        Shop.logOut(self.name)
	 
if __name__ == '__main__':
    ns = Pyro4.naming.locateNS()
    uri = ns.lookup("example.shop.Shop")
    print(uri)
    Shop = Pyro4.core.Proxy(uri)
    meeta = client('Meeta',50)
    rashmi = client('Rashmi',100)
    rashmi.doShopping_buying_a_book(Shop)
    meeta.doShopping_deposit_cash(Shop)
    print("")
    print("")
    print("")
    print("")
    
    print("The accounts in the %s:" % Shop.name())
    accounts = Shop.allAccounts()
    for name in accounts.keys():
              print("  %s : %.2f"\
                    % (name, accounts[name]))
