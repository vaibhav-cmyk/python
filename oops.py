# ABSTRACTION
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
    
#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("Car Started!!")


# car1=Car()
# car1.start()
# _____________________________________________________________________________________________________________
# ENCAPSULATION
# class Account:
#     def __init__(self,bal,acc):
#         self.balance= bal
#         self.acc_no=acc

#     def credit(self,amonut):
#         self.balance+=amonut
#         print("Rs",amonut,"was credited in your account!!")
#         print("total balance is",self.get_balance())

#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs",amount,"was debited from your account!!")
#         print("total balance is",self.get_balance())

#     def get_balance(self):
#         return self.balance
    

# acc1=Account(1000,12345)
# print(acc1.balance)
# acc1.credit(500)
# acc1.debit(100)
# print(acc1.get_balance())
# ____________________________________________________________________________________________________________

# INHERITANCE
# class Car:
#     color ="white"
#     def start(self):
#         print('car started')

#     def stop(self):
#         print("car stopped")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# c1=ToyotaCar("ritzz")
# print(c1.name)
# print(c1.color)
# c1.start()
# _____________________________________________________________________________________________________________


