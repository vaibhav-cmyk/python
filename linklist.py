class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printingNumbers(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def insert_beg(head, data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head

def insert_end(head, data):
    newNode = Node(data)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = newNode
    return head

def insert_random(head,data,index):
    newNode=Node(data)
    curr=head
    for i in range(index-1):
        curr=curr.next
    newNode.next=curr.next.next
    curr.next=newNode
    return head

def delete_beg(head):
    curr=head
    head=curr.next
    return head

def delete_end(head):
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head

def delete_random(head,index):
    curr=head
    for i in range(index-1):
        curr=curr.next
    curr.next=curr.next.next
    return head


# --- Example usage ---
a = Node(5)
b = Node(10)
a.next = b
head = a

printingNumbers(head)      

head = insert_beg(head, 15)
printingNumbers(head)       

head = insert_end(head, 20)
printingNumbers(head)       

head=insert_random(head,200,1)
printingNumbers(head)      

head=delete_beg(head)
printingNumbers(head)       

head=delete_end(head)
printingNumbers(head)

head=delete_random(head,1)
printingNumbers(head)

head=None