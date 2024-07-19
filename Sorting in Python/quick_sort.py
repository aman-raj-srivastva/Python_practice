def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    
def partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j

arr=[20,14,22,10,7] # len(arr)=5
quick_sort(arr,0,4)
print('Sorted array:',arr)

arr1=[20,14,22,10,7] # using arr1=arr even before calling the sort function for arr will also sort arr1, therefore arr1 is declared here separately 
quick_sort(arr1,1,3) # will sort only between given low and high index of array
print('Sorted array:',arr1)