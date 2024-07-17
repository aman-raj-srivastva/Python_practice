def binary(array,target):
    left,right=0,len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[32,70,81,93,107]  # sorted array
target=float(input('Enter the no. you want to search: '))
if binary(arr, target)==-1:
    print(target,'not available in the array.')
else:
    print(target,"found at index",binary(arr,target),'of the array.')