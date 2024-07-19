class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Creating nodes
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(10) # duplicate elements are allowed

# Connecting nodes to form a linked list
node1.next=node2
node2.next=node3
node3.next=node4
head=node1 # can be declared in each operation separately, for many operations at once I declared it here

# Printing the linked list
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print('None')

# adding a new node at the beginning
new_node=Node(50)
new_node.next=head
head=new_node

# Printing the linked list
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print('None')

# Adding a new node at the end
new_node=Node(50)
current=head
while current.next is not None:
    current=current.next
current.next=new_node

# Printing the linked list
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print('None')

# Adding new node at a specific position (here adding after 20)
current=head
new_node=Node(50)
while current is not None and current.data!=20:
    current=current.next
new_node.next=current.next
current.next=new_node

# Printing the linked list
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print('None')

# Deleting code from the beginning
if head is not None:
    head=head.next

# Printing the linked list
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print('None')

# Deleting Node from the end
current=head
while current.next.next is not None:
    current=current.next
current.next=None

# Printing the linked list
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print('None')

# Deleting a particular node
current=head
while current.next.data!=50:
    current=current.next
current.next=current.next.next

# Printing the linked list
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print('None')