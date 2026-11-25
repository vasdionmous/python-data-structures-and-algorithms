class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        # self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        # self.length += 1
        return True
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head 
        while fast and fast.next:
            # slow pointer is moving one step
            slow = slow.next 
            # fast pointer is moving two steps
            fast = fast.next.next 
        return slow 

    def has_loop(self):
        slow = self.head 
        fast = self.head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False 

    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next 
                    self.length -= 1
                else:
                    runner = runner.next 
            current = current.next 

    def binary_to_decimal(self):
        num = 0 
        current = self.head 
        # at the end of the loop num holds the decimal number equivalent of the binary number stored in the linked list
        while current:
            # shifts the binary digits left by one place (*2) and then adds the current digit
            num *= 2 + current.value 
            current = current.next 
        return num



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


my_linked_list = LinkedList(1)
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)

print(type(my_linked_list.head))