# Unrestricted account.
class Account(object):
    def __init__(self):
        self._balance = 0.0

    def pay(self, price):
        self._balance -= price

    def deposit(self, cash):
        self._balance += cash

    def balance(self):
        return self._balance


class Shop(object):
    def __init__(self):
        self.accounts = {}
        self.clients = ['Meeta','Rashmi','John','Ken']

    def name(self):
        return 'BuyAnythingOnline'

    def logOn(self, name):
        if name in self.clients :
            self.accounts[name] = Account()
        else :
            self.clients.append(name)
            self.accounts[name] = Account()

    def logOut(self, name):
        print('logout %s' %name)
   
    def deposit(self, name, amount):
        try:
            return self.accounts[name].deposit(amount)
        except KeyError:
            raise KeyError('unknown account')

    def balance(self, name):
        try:
            return self.accounts[name].balance()
        except KeyError:
            raise KeyError('unknown account')

    def allAccounts(self):
        accs = {}
        for name in self.accounts.keys():
            accs[name] = self.accounts[name].balance()
        return accs

    def buy(self,name,price):
        balance = self.accounts[name].balance()
        self.accounts[name].pay(price)
        


    
                

