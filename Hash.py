# Dictionary is hash table in Python, stores value at different location using a hash function with the key, thus reducing time complexity in accessing the key value pair
# Below is the code similar to dictionary with a hash function

# class HashTable:
#     def __init__(self):
#         self.max = 10
#         self.arr = [None for i in range(self.max)]  # hash table of size 10

#     def hash_func(self, key):  # creating a hash function
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.max

#     # __init__, __setitem__, __getitem__, __delitem__ are some standard operators in Python.
#     def __setitem__(self, key, val):  # using __setitem__ we can set item same as dictionary (look at the implementation), we dont explicitely need to set item using object t.__setitem__<or any other function name>('march 9',130) ; similarly for below functions/operators
#         h = self.hash_func(key)
#         self.arr[h] = val

#     def __getitem__(self, key):
#         h = self.hash_func(key)
#         return self.arr[h]

#     def __delitem__(self, key):
#         h = self.hash_func(key)
#         self.arr[h] = None


# t = HashTable()
# # t.__setitem__('march 9',130)
# t["march 9"] = 130 # m=109 + a=97 + r=114 + c=99 + h=104 + <space>=32 + 9=57 = 612 ---> 612%10 = 2; therefore 'march 9' is placed at 2nd index in the hash table, similarly for others also
# t["july 18"] = 530
# t["feb 17"] = 200
# print(t["feb 17"])
# print(t["dec 17"])  # not assigned therefore print None
# print(t.arr)
# del t["july 18"]
# print(t.arr)
# print(t)

# # print(ord('9'))
# # print(sum([109,97,114,99,104,32,57]))

# t['june 19']=450 # here this will take 9th index in hash table, colliding with key 'march 9'
# print(t.arr) # if two keys are colliding with same index number than the first assignment will change for new assignment
# print(t['march 9']) # same as print(t['june 19']); due to collision this will print 450, even though it has its own value=130


# --------------------------------------------Collision Handling-----------------------------------------------------------------
class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]  # changing None to empty list

    def hash_func(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.hash_func(key)
        found = False
        for index, element in enumerate(self.arr[h]): # for updating
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.hash_func(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.hash_func(key)
        for index, element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]

t=HashTable()
t['march 6']=128
t['march 6']=78 # updating the key value
t['march 8']=67
t['march 9']=4
t['march 17']=459 # 'march 6' and 'march 17' as single element with index 9, No collision
print(t.arr)
print(t['march 6']) # No compromise to value data
