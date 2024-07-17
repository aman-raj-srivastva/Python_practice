def insertion(arr1):
    n=len(arr1)
    for i in range (1,n):
        key=arr1[i]
        j=i-1
        while j>=0 and key<arr1[j]: # to print in desending order use key>arr1[j]
            arr1[j+1]=arr1[j]
            j-=1
        arr1[j+1]=key

arr=[20,14,22,10,7] # len(arr)=5                for understanding --->  i=4, j=-1, key=7, [7,10,14,20,22]
insertion(arr)
print('Sorted array:',arr)
