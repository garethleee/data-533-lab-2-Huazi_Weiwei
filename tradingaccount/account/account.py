from datetime import datetime
import pandas as pd

class Account():
    def __init__(self,balance):
        self.balance=balance
        ##create dict {stockname:stockbalance} to track stocks in account
        self.stock={}
        #create data frame to record the transaction log of the money and stock activity
        self.account_history=pd.DataFrame(columns=['Balance','Action','Amount','Date','Previous_Balance'])
        self.stock_history=pd.DataFrame(columns=['Balance','Action','Amount','Price','Date','Previous_Balance','Commission'])
        
    def withdraw(self,amount,date=datetime.now()):  ##if date parameter not passed, use datetime.now()
        if self.balance>=amount:
            previous_balance=self.balance
            self.balance=self.balance-amount
            new_record=pd.Series([self.balance,'withdraw',amount,date,previous_balance],
                                 index=['Balance','Action','Amount','Date','Previous_Balance'])
            self.account_history=self.account_history.append(new_record,ignore_index=True)
            return True
        else:
            print('Current balance is insufficient for withdraw %d' % amount)
            
    def deposit(self,amount,date=datetime.now()):
        previous_balance=self.balance
        self.balance=self.balance+amount
        new_record=pd.Series([self.balance,'deposit',amount,date,previous_balance],
                                 index=['Balance','Action','Amount','Date','Previous_Balance'])
        self.account_history=self.account_history.append(new_record,ignore_index=True)
        return True

