# creates a list element
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# creates a singly linked list with methods: print, append, pop, prepend, pop_first, get, set_value, insert, remove, and reverse
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        # prints each value in the linked list
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def append(self, value):
        # creates a node and adds it at the end of the linked list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # pops a node from the end of the linked list
        # case: list has 0 elements
        if self.length == 0:
            return None 
        # case: list has (at least) 2 elements 
        pre = self.head 
        temp = self.head 
        while(temp.next):
            pre = temp 
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None 
        self.length -= 1

        # case: list has 1 element
        if self.length == 0:
            self.head = None 
            self.tail = None 

        return temp

    def prepend(self, value):
        # creates a node and adds it to the start of the linked list
        new_node = Node(value)
        # handles an empty linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node 
        self.length += 1 
        return True

    def pop_first(self):
        # removes and returns the first node in the linked list
        # case: list has 0 elements
        if self.length == 0:
            return None
        # case: list has (at least) 2 elements 
        temp = self.head
        self.head = temp.next 
        self.length -= 1
        # case: list has 1 element
        if self.length == 0:
            self.head = None 
            self.tail = None 
        return temp

    def get(self,index):
        # returns the node at the given index
        # tests to see if index is valid 
        if index < 0 or index >= self.length:
            return None 
        temp = self.head 
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # updates the value at the given index
        temp = self.get(index)
        if temp:
            temp.value = value 
            return True 
        return False
    
    def insert(self, index, value):
        # creates a node and inserts it at the given index
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1
        return True 

    def remove(self,index):
        # removes and returns the node at the given index
        if index <0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = self.get(index-1)
        # temp = self.get(index) # costs O(n)
        temp = pre.next 
        pre.next = temp.next 
        temp.next = None 
        self.length -= 1
        return pre 

    def reverse(self):
        # reverses the order of the nodes in the linked list
        temp = self.head 
        self.head = self.tail 
        self.tail = temp 
        after = temp.next 
        before = None 
        for _ in range(self.length):
            after = temp.next 
            temp.next = before 
            before = temp 
            temp = after 