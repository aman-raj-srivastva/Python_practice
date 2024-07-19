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
def ll_print():
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
ll_print()

# Adding a new node at the end
new_node=Node(50)
current=head
while current.next is not None:
    current=current.next
current.next=new_node
# Printing the linked list
ll_print()

# Adding new Node at a specific position
def add_after_value(data_after, data_to_insert):
    current=head
    new_node=Node(data_to_insert)
    while current is not None and current.data!=data_after:
        current=current.next
    new_node.next=current.next
    current.next=new_node
add_after_value(20,50)
# Printing the linked list
ll_print()

# Deleting Node from the beginning
if head is not None:
    head=head.next
# Printing the linked list
ll_print()

# Deleting Node from the end
current=head
while current.next.next is not None:
    current=current.next
current.next=None
# Printing the linked list
ll_print()

# Deleting a particular node
def delete_node(node_to_delete):
    current=head
    while current.next.data!=node_to_delete:
        current=current.next
    current.next=current.next.next
delete_node(50)
# Printing the linked list
ll_print()

# Adding a list at end
def list_add(list):
    for i in range(len(list)):
        new_node=Node(list[i])
        current=head
        while current.next is not None:
            current=current.next
        current.next=new_node       
list=['aman',23,34]
list_add(list)
# Printing the linked list with count
current=head
count=0
while current is not None:
    print(current.data, end='->')
    count+=1
    current=current.next
print('None')
print('Count of this Linklist is',count)