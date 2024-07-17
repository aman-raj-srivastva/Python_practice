def bubble (arr):
    n=len(arr)
    for i in range (n):
        swapped=False
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swapped=True
        if not swapped:
            break
                                                        
arr=[20,14,22,10,7] # len(arr)=5
bubble(arr)
print('Sorted array:',arr)