import random
class User:
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password
        self.balance=0
        self.loan=0
        self.transaction_id=[]
        print(f'User Login Account')
        
 
    def create(self,Email,Password):
        if self.email==Email and self.password==Password:
            print(f'User Login Succseful')
        else:
            print(f'Your email or password incorrect')

    def deposit(self,amount):
        if(amount>0):
            self.balance +=amount
            print(f'Deposited {amount}. New balance: {self.balance}')
        else:
            print(f'Invalid amount for deposit.')

    def  withdraw(self,amount):
        if amount > 0  and amount<=self.balance:
            self.balance -=amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        else:
            print(f'Invild amount for withdrew or insufficient balance.')

    def available_balance(self):
        print(f'Account balance:-> {self.balance}')

    def transfar_amount(self,amount):
            if amount>0 and self.balance >=amount:
                print(f'Your tarnsfar Amount {amount}')
                self.balance -=amount
                random_intger = random.randint(100000,200000)
                self.available_balance()
                print(f'Succesful transfar . Your transaction id: {random_intger}')
                self.transaction_id.append(random_intger)
            else:
                print(f'Your balance not available.')

    def check_tran(self):
        for id in self.transaction_id:
            print(id)

    def Total(self):
        return self.balance
    
    def Loan(self,amount,loan_feature):
        if amount>0 and self.balance*2 >=amount and loan_feature==True:
            self.balance +=amount
            self.loan=amount
            print(f'Loan amount {amount} Your balance {self.balance}')
        elif loan_app==False:
            print(f'Off the loan feature')
        else:
            print(f'Your balance not available.')

    def loan_amount(self):
        return self.loan

class admin:
    def __init__(self,email,password) -> None:
        self.password=password
        self.email=email
        self.users=[]
        self.total=0
        self.total_loan=0
        print(f'Admin Login Account')

    def create(self,Email,Password):
        if self.email==Email and self.password==Password:
            print(f'Admin Login Succseful')
        else:
            print(f'Your email or password incorrect')
    
    def add_user(self,user,amount,loan):
        self.users.append(user)
        self.total +=amount
        self.total_loan +=loan
 
    def Bank_balance(self):
        print(f'Bank_balance {self.total}')
    
    def Bank_Loan(self):
        print(f'Total loan amount: {self.total_loan}')
    
    def loan_feature(self):
        return True
  
user_1=User('sunny@123',123)
user_1.create('sunny@123',123)
user_1.deposit(100)
user_1.available_balance()

user_2 = User('kamrul@12',234)
user_2.create('kamrul@12',234)
user_2.deposit(120)
user_2.available_balance()


Admin=admin('snn@134',123)
Admin.create('snn@134',123)
loan_application = Admin.loan_feature()
user_1.Loan(100,loan_application)
user_2.Loan(60,loan_application)
Admin.add_user(user_1,user_1.Total(),user_1.loan_amount())
Admin.add_user(user_2,user_2.Total(),user_2.loan_amount())
Admin.Bank_Loan()
Admin.Bank_balance()
