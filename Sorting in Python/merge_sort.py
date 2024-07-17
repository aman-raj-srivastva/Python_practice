def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid=len(arr)//2
    l_half=arr[:mid]
    r_half=arr[mid:]
    l_half=merge_sort(l_half)
    r_half=merge_sort(r_half)
    return merge(l_half, r_half)

def merge(left,right):
    # print('1st',left,right)
    new=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
            # print(left,'i=',i)
        else:
            new.append(right[j])
            j+=1
            # print(right,'j=',j)
    new.extend(left[i:])
    new.extend(right[j:])
    print('2nd',new)
    return new

arr=[20,14,22,10,7] # len(arr)=5
sorted_arr=merge_sort(arr)  # Capture the sorted array
print('Sorted array:',sorted_arr)