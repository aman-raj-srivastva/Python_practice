# name of this file is changed to numpy_practice.py from numpy because it was shadowing the actual numpy.py installed
import numpy as np

# list1=[12,10,11,9,82,11]
# array1=np.array(list1)
# print(array1)
# print(type(array1))

# list1=[12,10,11,9.01,82,11] # here when I changed only one element from int to float then all the elements of int changed to float, with same space taking after the decimal place
# array1=np.array(list1)
# print(array1)
# # or you can do the above changes using the following code too
# list1=[12,10,11,9,82,11]
# array1=np.array(list1, dtype=float)
# print(array1)

# # similarly
# list1=[12,10,11,'9',82,11] # here when I changed only one element from int to string then all the elements of int changed to string
# array1=np.array(list1)
# print(array1)
# # or you can do the above changes using the following code too
# list1=[12,10,11,9,82,11]
# array1=np.array(list1, dtype=str) # we can also use 'U32' or 'U16' instead of str
# print(array1)

# ij ---> 00 01 02   10 11 12  20 21 22
# list1=[[12,90,73],[23,32,6],[77,32,76]] # 2D array, each nested list shd have same no. of elements
# array1=np.array(list1)
# print(array1)

# array1=np.arange(1,11) # 1D array
# print(array1)
# array1=np.arange(11,17).reshape(2,3) # 2D array, .reshape(row,column) the range given shd be such that each place of the array shd be filled with an element
# print(array1)

# array1=np.zeros(4) # 1D array
# print(array1)
# # array1=np.zeros(4,2) Wrong Way
# array1=np.zeros((4,2)) # Right Way for 2D array
# print(array1)
# # similarly for ones
# array1=np.ones(4) # 1D array
# print(array1)
# array1=np.ones((4,2)) # 2D array
# print(array1)

# list1=[12.2,10,11,9,82,11]
# list2=[12,'90',73],[23,32,6],[77,32,76],[44,55,23]
# list3=[[12,90,73]],[[23,32,6]],[[77,32,76]],[[6,8,9]]
# array1=np.array(list1)
# array2=np.array(list2)
# array3=np.array(list3)
# print('Printing array1:\n',array1)
# print('The no. of dimension in array1 is',array1.ndim) # prints dimension of array1
# print('The shape of array1 is',array1.shape) # prints shape of array1 (row,)
# print('The size of array1 is',array1.size) # prints total no. of elements in array1
# print('The itemsize of array1 is',array1.itemsize) # prints the size of datatype in array1
# print('The dtype of array1 is',array1.dtype) # prints datatype of array1
# print('Printing array2:\n',array2)
# print('The no. of dimension in array2 is',array2.ndim) # prints dimension of array2
# print('The shape of array2 is',array2.shape) # prints shape of array2 (row,column)
# print('The size of array2 is',array2.size) # prints total no. of elements in array2
# print('The itemsize of array2 is',array2.itemsize) # prints the size of datatype in array2
# print('The dtype of array2 is',array2.dtype) # prints datatype of array2
# print('Printing array3:\n',array3)
# print('The no. of dimension in array3 is',array3.ndim) # prints dimension of array3
# print('The shape of array3 is',array3.shape) # prints shape of array3 (row,column,depth)
# print('The size of array3 is',array3.size) # prints total no. of elements in array3
# print('The itemsize of array3 is',array3.itemsize) # prints the size of datatype in array3
# print('The dtype of array3 is',array3.dtype) # prints datatype of array3

# Indexing/slicing in 1D array is same as list
# arr1=np.array([19,22,34,12,55,39])
# print(arr1[-3])
# print(arr1[-1:-4:-2])
# print(arr1[0:])
# print(arr1[-3:])
# print(arr1[::-1])
# # Indexing/slicing in 2D array, draw the matrix for understanding
# array1=np.array([[12,23,13], [22,34,13], [43,55,22], [1,5,3]]) # 4X3 matrix
# '''        0   1   2
#       ------------------
#   0-> |   12  23  13   |
#   1-> |   22  34  13   |
#   2-> |   43  55  22   |
#   3-> |    1   5   3   |
#       ------------------
# '''
# print(array1[1,2])
# print(array1[0,])
# print(array1[0,:])
# print(array1[:,2])
# print(array1[:,])
# print(array1[1:3,1:3]) # submatrix, here 3 is exclusive as it is the end limit of range
# print(array1[1:10,1:100]) # out of league but still prints without error
# print(array1[1:3,])
# print(array1[:,1:3])
# print(array1[1:4,1])
# print(array1[1:4,:1])

# Arithmetic operations on numpy
# arr=np.array([[11,2,3],[12,34,21]]) # 2X3
# arr2=np.array([[8,5,10],[2,4,1]]) #2X3
# print(arr+arr2)
# print(arr-arr2)
# print(arr/arr2)
# print(arr//arr2)
# print(arr%arr2)
# print(arr2*arr) # its not matrix wise multiplication, its element to element multiplication
# # print(arr2 @ arr) # it is a matrix multiplication; give error as both arr2 and arr are 2X3
# arr3=np.array([[12,5],[2,4],[10,0]]) # 3X2
# print(arr3 @ arr) # result 3X3 matrix
# print(arr3.transpose())

# Sorting
# arr1=np.array([69,10,83,24,77,25])
# sort=np.sort(arr1)
# print(sort) # by default ascending order
# sort_desc=np.sort(arr1)[::-1]
# print(sort_desc) # descending order
# argsort=np.argsort(arr1)
# print(argsort) # ***This returns actual index value of elements after sorting***
# print(arr1) # No changes in actual array
# arr1.sort()
# print(arr1,'\n') # inplace sorting (actual array lost, now it is a sorted array)
# # Sorting in 2D array
# arr=np.array([[81,3,10],[25,45,11],[28,14,12]]) #2X3
# print(np.sort(arr)) # row wise sorting (by dafault, axis=1)
# print(np.sort(arr,axis=0)) # column wise sorting 
# print(np.sort(arr,axis=0)[::-1]) # column wise sorting, reverse 
# argsort2=np.argsort(arr)
# print(argsort2)
# argsort2=np.argsort(arr,axis=0)
# print(argsort2)
# arr.sort()
# print(arr)
# arr.sort(axis=0)
# print(arr)

# Statistical operations on array
x=np.array([12,22,10,34,5,15])
print(np.max(x))
print(np.min(x))
print(np.sum(x))
print(np.mean(x))
print(np.median(x)) # first sorted then middle value
print(np.prod(x)) #product
print(np.var(x)) #variance = mean-each element ke square ka addition divided by total no. of elements
print(np.std(x)) #standard Variance (square of variance)