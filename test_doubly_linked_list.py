from doubly_linked_list import DoublyLinkedList


print("Create the doubly linked list")
my_linked_list = DoublyLinkedList(1)
for i in range(2, 10):
    my_linked_list.append(i)

my_linked_list.print_list()

print("\nAppend value 10")
my_linked_list.append(10)
my_linked_list.print_list()

print("\nPop the last value")
popped = my_linked_list.pop()
print("Popped:", popped.value)
my_linked_list.print_list()

print("\nPrepend value 0")
my_linked_list.prepend(0)
my_linked_list.print_list()

print("\nPop the first value")
popped_first = my_linked_list.pop_first()
print("Popped:", popped_first.value)
my_linked_list.print_list()

print("\nGet the value at index 3")
node = my_linked_list.get(3)
print("Value:", node.value)

print("\nSet index 3 to 30")
my_linked_list.set_value(3, 30)
my_linked_list.print_list()

print("\nInsert value 25 at index 4")
my_linked_list.insert(4, 25)
my_linked_list.print_list()

print("\nRemove the value at index 4")
removed = my_linked_list.remove(4)
print("Removed:", removed.value)
my_linked_list.print_list()

print("\nReverse the doubly linked list")
my_linked_list.reverse()
my_linked_list.print_list()
