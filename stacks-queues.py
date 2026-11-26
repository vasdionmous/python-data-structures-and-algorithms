# stacks are LIFO = last-in, first-out

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
            # prints each value in the stack
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next 
    
    # similar to prepend
    def push(self, value):
        # pushes a node onto the stack
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node 
        self.height += 1
        return True 

    def pop(self):
        # pops a node from the top of the stack
        if self.height == 0:
            return None 
        temp = self.top 
        self.top = self.top.next 
        temp.next = None 
        self.height -= 1
        return temp.value

# queue are FIFO = first-in, first-out

# in lls appending is O(1) and popping from the beginning is O(1)
# ll: O -> O -> O -> O ->
# queue: first: O - O - O - O: last
# enqueue = appending
# dequeue = pop_first

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        # prints each value in the queue
        temp = self.first 
        while temp is not None:
            print(temp.value)
            temp = temp.next   

    def enqueue(self,value):  
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node 
            self.last = new_node 
        self.length += 1
        return True 

    def dequeue(self):
        if self.length == 0:
            return None 
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None 
        else:
            self.first = self.first.next 
            temp.next = None 
        self.length -= 1 
        return temp.value 