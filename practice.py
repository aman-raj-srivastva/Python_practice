# import pyttsx3
# engine = pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.say("Hello")
# engine.runAndWait()

# import os
# dir="/"
# contents=os.listdir(dir)
# for item in contents:
#     print(item)

# a=3.50000000001
# b=-4
# print(abs(b))

# a+=5
# print(round(a))
# str="ha Ha Ha ha"
# print(str.replace('Ha','Na'))
# print (len(str))

# d=['aftab','adil','v']
# d[3]='a'
# print(d)
# print('-'.join(d))

# str="hnm-olo-poe"
# print(str.split('-'))

# st={'name':"hui",'age':12}
# print(st("name"))

# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# courses=('coa','dsa')
# info={'name':'aman','lastname':'raj'}
# func(courses,info)    

# with open("tst.txt","r") as f:
#     print(f.name)
# print(f.closed)

# num=input('enter a no. ')
# print(num)
# print(type(num))
# print(num+'2')

# num=int(input('enter a no. '))
# print(num)
# print(type(num))
# print(num+2)

# num=bool(input('enter a no. '))
# print(num)

# byte=bytearray([65,77,97])
# byte[2]=100
# print(byte)

# a=1
# a=2
# print(a)

# print (2**3**2)
# print(bool(7>8)==False==True)

# print(~82828)

# x=[2]
# y=[2]
# print(x is y)

# a=[1,3,7,4]
# print(1 in a)

# str='hello2hello'
# # print(str.title())
# # print(str.count('hello'))
# print(str.isalnum())

# str='   Hello World!   '
# str2='-'
# print(str.lstrip())
# print(str.rstrip())
# print(str.replace('World','Earth')) 
# print(str2.join(str))

# li1=list()
# print(li1)
# str='aeiou'
# li1=list(str)
# print(li1)
# li1.pop(3)
# print(li1)

# a=print('12')
# print(a)

# def f():
#     print('hi')
# f()

# a=3
# b=5
# a,b=b,a # swaping
# print(a,b) 

# list1=[i**2 for i in range(15) if i%2==0] # List comprehension
# print(list1)
# dict1={i:i*i for i in range(15) if i%2==0} # Dictionary comprehension
# print(dict1)

# numbers=list(range(1,101)) # can also be done with loops (extending an empty list one by one with current integer values)
# print(numbers)
# import sys
# print(sys.getsizeof(numbers))
# print([num*2 for num in numbers]) # List comprehension
# # using generator below for memory efficiency
# def creater():
#     i=1
#     while i<=200:
#         yield i
#         i+=1
# print(creater())
# x=creater()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(list(x))

# # append() VS extend() --> list operations:
# list=[1,2,3,4]
# # print(list.append(100)) # --> None
# list.append(100) # --> one at a time
# print(list)
# # list.append(100,200) # --> TypeError
# list.append([100,200])
# print(list) 
# list=[1,2,3,4]
# list.extend([100,200])
# print(list)
# # add() VS update() --> set operations:
# set={1,3,5,7,9}
# set.add(11) # --> one at a time, can be unordered
# print(set)
# set.add(5)
# print(set)
# set.update({13,17}) 
# print(set)

# import pandas as pd
# scores=[('Pinku',95),('Sonu',90),('Tapu',55),('Goli',77)]
# df=pd.DataFrame(scores, columns=('Name','Marks'))
# def grade (marks):
#     if marks > 90:
#         return 'A'
#     elif 80< marks <= 90:
#         return 'B'
#     elif 70< marks <= 80:
#         return 'c'
#     elif 60< marks <= 70:
#         return 'D'
#     else:
#         return 'F'
# grades=map(grade,df.Marks)
# grades=list(grades)
# df.insert(2,'Grade',grades)
# print(df)
# failed=df.Marks<60
# print('Failed students:\n',df[failed])

# marks=[67,77,89,34,65,55]
# def fail(score):
#     return score<60
# result=filter(fail,marks)
# print('Failing Scoores:',list(result))

# city=['jaipur','kota','chandigarh','delhi','muzaffarpur']
# def length(city):
#     return len(city)
# sort=sorted(city, key=length, reverse=True)
# print('Sorted city by word length in reverse:',sort)
# # or
# city=['jaipur','kota','chandigarh','delhi','muzaffarpur']
# sort=sorted(city, key=lambda x: len(x),reverse=True)
# print('Sorted city by word length in reverse:',sort)

# def decorator(func):
#     def wrapper():
#         print('Transaction initiated...')
#         func()
#         print('Transaction ended...')
#     return wrapper
# def transaction():
#     print("...Executing steps of transaction1...\nPlease wait!")
# # Applying the decorator
# trans1 = decorator(transaction)
# # Invoking the decorated function
# trans1()
# @decorator
# def transaction():
#     print("...Executing steps of transaction2...\nPlease wait!")
# transaction()

import statistics
import time
start_tym=time.time()
data=[12,45,23,78,90,102,67]
mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
var=statistics.variance(data)
stdev=statistics.stdev(data)
print(f"Mean: {mean}\nMedian: {median}\nMode: {mode}\nVariance: {var}\nStandard Deviation: {stdev}")
end_tym=time.time()
total_tym=end_tym-start_tym
print('Total time taken (in seconds):',total_tym)