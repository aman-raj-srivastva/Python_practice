class queue:
    def __init__(self):
        self.values=[]
    def enqueue(self,x):
        # self.values.extend(x) # not used here because queue add only one element at a time (acc. to me)
        self.values.append(x) 
    def dequeue(self):
        front=self.values[0]
        self.values=self.values[1:]
        return front
q=queue()
q.enqueue(7)
q.enqueue(5)
q.enqueue(7)
q.enqueue(9)
print(q.values)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())