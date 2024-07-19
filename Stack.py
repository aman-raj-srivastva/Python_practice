class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values=[x]+self.values
    def pop(self):
        return self.values.pop(0)
s=stack()
s.push(5)
s.push(76)
s.push(56)
s.push(40)
print(s.values)
print(s.pop())
print(s.pop())
print(s.values)