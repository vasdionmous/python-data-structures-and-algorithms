# creates a list element
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 
# creates a doubly linked list with methods: print,
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1

    def print_list(self):
        # prints each value in the doubly linked list
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        # creates a node and adds it at the end of the linked list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            new_node.prev = self.tail
            self.tail = new_node 
        self.length += 1
        return True

    def pop(self):
        # pops a node from the end of the linked list
        # case: list has 0 elements
        if self.length == 0:
            return None 
        temp = self.tail 
        # case: list has 1 element
        if self.length == 1:
            self.head = None 
            self.tail = None 
        # case: list has 2+ elements
        else:
            self.tail = self.tail.prev
            self.tail.next = None 
            temp.prev = None 
        self.length -= 1
        return temp

    def prepend(self,value):
        # creates a node and adds it to the start of the linked list
        new_node = Node(value)
        # handles an empty linked list
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
        self.length += 1 
        return True 

    def pop_first(self):
        # removes and returns the first node in the linked list
        if self.length == 0:
            return None
        temp = self.head
        # case: list has 1 element
        if self.length == 1:
            self.head = None 
            self.tail = None 
        # case: list has 2+ element
        else: 
            self.head = self.head.next 
            self.head.prev = None 
            temp.next = None 
        self.length -= 1
        return temp

    def get(self,index):
        # returns the node at the given index
        # tests to see if index is valid 
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        # optimizing the singly-linked-list code
        # index appears in the first half of the list
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail 
            # range(start, stop, step)
            # range(5,0,-1) returns 5, 4, 3, 2, 1
            # range(0,10,2) returns 0, 2, 4, 6, 8
            for _ in range(self.length-1,index,-1):
                temp = temp.prev 
        return temp

    def set_value(self, index, value):
        # updates the value at the given index
        # exactly the same code as in the singly-list-case (although depends on get whose code differs)
        temp = self.get(index)
        if temp is not None:
            temp.value = value 
            return True 
        return False 

    def insert(self,index,value):
        # creates a node and inserts it at the given index
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        # after = self.get(index-1) # makes it O(n)
        after = before.next # makes it O(1)
        new_node.prev = before 
        new_node.next = after  
        before.next = new_node
        after.prev = new_node 
        self.length += 1 
        return True

    def remove(self,index):
        # removes and returns the node at the given index 
        if index <0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()        
        temp = self.get(index)     
        before = temp.prev 
        after = temp.next 
        before.next = after # temp.prev.next = temp.next
        after.prev = before #temp.next.prev = temp.prev 
        temp.next = None 
        temp.prev = None 
        self.length -= 1 
        return temp 

        
    def reverse(self):
        # reverses the order of the nodes in the doubly linked list
        temp = self.head
        self.head, self.tail = self.tail, self.head

        while temp is not None:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev