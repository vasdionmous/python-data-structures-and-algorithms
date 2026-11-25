class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
     
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
def find_kth_from_end(ll, k):       
    slow = ll.head 
    fast = ll.head 
    for _ in range(k):
        # list is shorter than k
        if fast is None:
            return None 
        fast = fast.next 
    while fast:
        slow = slow.next 
        fast = fast.next 
    return slow 

ll = LinkedList(1)
for i in range(2,6):
    ll.append(i)

result = find_kth_from_end(ll,2)
print(result.value)