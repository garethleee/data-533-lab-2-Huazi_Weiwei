from .account import Account
import pandas as pd
from datetime import datetime

class cnAccount(Account):
    def __init__(self,balance):
        ##inherit from Account class
        Account.__init__(self,balance)

    def withdraw(self,amount,date=datetime.now()):
        Account.withdraw(self,amount,date)

    def deposit(self,amount,date=datetime.now()):
        Account.deposit(self,amount,date)

    def buy(self,stock,amount,price,date=datetime.now()):
              #if buy money amount over 20000, the commision fee is amount*0.00025, if under
              #20000, the commission fee is 5.
        if amount*price>20000:
            ##check if there is enough money to buy and pay the commission fee
            if self.balance>=amount*price+amount*price*0.00025:
                previous_balance=self.balance
                self.balance=self.balance-amount*price-amount*price*0.00025
                commission=amount*price*0.00025
                ## if this is first time to buy this stock, add a new dict pair in self.stock
                if stock not in self.stock.keys():
                    self.stock[stock]=amount
                else:
                    self.stock[stock]+=amount
                new_record=pd.Series([self.balance,'buy',stock,amount,price,date,previous_balance,commission],
                                 index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                return True
            else:
                print('Current balance is insufficient for buying %d of %s at %f' % (amount,stock,price))
        else:
            if self.balance>=amount*price+5:
                previous_balance=self.balance
                self.balance=self.balance-amount*price-5
                commission=5
                if stock not in self.stock.keys():
                    self.stock[stock]=amount
                else:
                    self.stock[stock]+=amount
                new_record=pd.Series([self.balance,'buy',stock,amount,price,date,previous_balance,commission],
                                 index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                return True
            else:
                print('Current balance is insufficient for buying %d of %s at %f' % (amount,stock,price))

    def sell(self,stock,amount,price,date=datetime.now()):
        ##check if there is stock in account for selling
        if stock not in self.stock.keys():
            print('No %s in the account' % stock)
        else:
            if self.stock[stock]>=amount:
                if amount*price>20000:
                    previous_balance=self.balance
                    self.balance=self.balance+amount*price-amount*price*0.00025
                    commission=amount*price*0.00025
                    self.stock[stock]-=amount
                    new_record=pd.Series([self.balance,'sell',stock,amount,price,date,previous_balance,commission],
                                     index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                    self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                    return True
                else:
                    previous_balance=self.balance
                    self.balance=self.balance+amount*price-5
                    commission=5
                    self.stock[stock]-=amount
                    new_record=pd.Series([self.balance,'sell',stock,amount,price,date,previous_balance,commission],
                                     index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                    self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                    return True
            else:
                print('Current balance is insufficient for selling %d of %s at %f' % (amount,stock,price))
