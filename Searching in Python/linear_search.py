def linear (arr, target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return -1
    
array=[23,12,90,34.4,22]
target=float(input('Enter the no. you want to search: '))
if linear(array, target)==-1:
    print(target,'not available in the array.')
else:
    print(target,"found at index",linear(array,target),'of the array.')