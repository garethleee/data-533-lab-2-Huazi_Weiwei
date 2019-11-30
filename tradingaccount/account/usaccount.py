from account import Account
import pandas as pd
from datetime import datetime

#the commission fee is 1 usd for 1 transaction
class usAccount(Account):
    def __init__(self,balance):
        Account.__init__(self,balance)

    def withdraw(self,amount):
        Account.withdraw(self,amount)

    def deposit(self,amount):
        Account.deposit(self,amount)

    def buy(self,stock,amount,price,date=datetime.now()):
        if self.balance>=amount*price+1:
                previous_balance=self.balance
                self.balance=self.balance-amount*price-1
                commission=1
                if stock not in self.stock.keys():
                    self.stock[stock]=amount
                else:
                    self.stock[stock]+=amount
                new_record=pd.Series([self.balance,'buy',amount,price,date,previous_balance,commission],
                                 index=['Balance','Action','Amount','Price','Date','Previous_Balance','Commission'])
                self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                return True
        else:
            print('Current balance is insufficient for buying %d of %s at %f' % (amount,stock,price))

##selling stock even when there is not any in the account is permitted in US market.
    def sell(self,stock,amount,price,date=datetime.now()):
        if stock not in self.stock.keys():
            self.stock[stock]=0
        if (self.stock[stock]-amount)*price+self.balance>=1:
            previous_balance=self.balance
            self.balance=self.balance+amount*price-1
            commission=1
            self.stock[stock]-=amount
            new_record=pd.Series([self.balance,'sell',amount,price,date,previous_balance,commission],
                                     index=['Balance','Action','Amount','Price','Date','Previous_Balance','Commission'])
            self.stock_history=self.stock_history.append(new_record,ignore_index=True)
            return True
        else:
            print('Current balance is insufficient for selling %d of %s at %f' % (amount,stock,price))
