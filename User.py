import random
class User:
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password
        self.balance=100
        self.transaction_id=[]
        self.user=[]
    print(f'login account')
    def create(self,Email,Password):
        if self.email==Email and self.password==Password:
            self.user.append(Email)
            print(f'login succseful')
        else:
            print(f'your email or password ancorrect')

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
        print(f'Account balance: {self.balance}')

    def transfar_amount(self,amount):
            if amount>0 and self.balance >=amount:
                print(f'your tarnsfar amount {amount}')
                self.balance -=amount
                random_intger = random.randint(10000,20000)
                self.available_balance()
                print(f'Succesful transfar . your transaction id {random_intger}')
                self.transaction_id.append(random_intger)
            else:
                print(f'your balance not available.')

    def check_tran(self):
        for id in self.transaction_id:
            print(id)

class admin:
    def __init__(self,name,email) -> None:
        self.name=name
        self.email=email
    print(f'login account')

    def create(self,Email,Password):
        if self.email==Email and self.password==Password:
            print(f'login succseful')
        else:
            print(f'your email or password ancorrect')
    
    def total(self):
        total=0
        for id in self.user:
            total +=id.available_balance
        print(total)
user_1=User('sunny@123',123)
user_1.create('sunny@123',123)
user_1.deposit(100)
user_1.withdraw(120)
user_1.available_balance()
user_2 = User('kamrul@12',234)
user_2.create('kamrul@12',234)
user_2.deposit(120)
user_2.available_balance()
user_2.transfar_amount(10)
user_2.transfar_amount(34)
user_2.transfar_amount(36)
user_2.check_tran()
islam =admin('islam@12',123)
islam.create('islam@12',123)
islam.total()