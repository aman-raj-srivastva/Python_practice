# class first:
#     x=7
# obj=first()
# print(obj.x)

# class employee:
#     def putdata(self):                                                # method 1
#         self.id=int(input('Enter employee id: '))
#         self.name=input('Enter employee name: ')
#         self.salary=float(input('Enter employee salary: '))
#     def display(self):                                                # method 2
#         print('Employee id:',self.id)
#         print('Employee name:',self.name)
#         print('Employee salary:',self.salary)
# a=employee() 
# a.putdata()
# a.display()

# class employee:
#     def __init__(self):                                               # Constructor
#         self.id=int(input('Enter employee id: '))
#         self.name=input('Enter employee name: ')
#         self.salary=float(input('Enter employee salary: '))
#     def display(self):                                                # method 2
#         print('Employee id:',self.id)
#         print('Employee name:',self.name)
#         print('Employee salary:',self.salary)
# a=employee() 
# a.display()     # No need to call putdata method

# class student:
#     def __init__(self,roll,name,marks):  # dunder init function (paramaterized constructor)
#         self.rollno=roll                 # |...
#         self.name=name                   #      > Property
#         self.marks=marks                 # |'''
#     def avg(self):      # method
#         return(sum(self.marks)/len(self.marks))
# first_student=student(12,'Tapu',[50,55,65,34,25,71])
# print(first_student.name)
# print(first_student.avg())

# Inheritance:
class OTTsub:
    def __init__(self,sub_id,plan,total_payment):
        self.id=sub_id
        self.plan=plan
        self.payment=total_payment
    def subscribe(self):
        print(f'Subscriber with id {self.id} paid ${self.payment} for {self.plan} plan.')
    def unsubscribe(self):
        print(f'Subscriber with id {self.id} unsubscribed from the {self.plan} plan.')
myott=OTTsub(56743,'monthly',200)
myott.subscribe()
myott.unsubscribe()
class PremiumSub(OTTsub):
    def __init__(self, sub_id, plan, total_payment, devices):
        super().__init__(sub_id, plan, total_payment)
        self.max_devices=devices
    def set_max_devices(self, devices):
        self.max_devices=devices
        print(f'Maximum devices set to {self.max_devices} in the Premium plan.')
Netflix=PremiumSub(12345,'yearly',1200,1)
Netflix.subscribe()
Netflix.set_max_devices(4)

