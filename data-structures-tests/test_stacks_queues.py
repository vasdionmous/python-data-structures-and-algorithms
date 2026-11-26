from pathlib import Path
from runpy import run_path


stack_queue = run_path(
    str(Path(__file__).resolve().parents[1] / "data-structures" / "stacks-queues.py")
)
Stack = stack_queue["Stack"]
Queue = stack_queue["Queue"]

print("Create the stack")
my_stack = Stack(1)
my_stack.push(2)
my_stack.print_stack()

print("\nPop the top value")
popped = my_stack.pop()
print("Popped:", popped)
my_stack.print_stack()

print("\nCreate the queue")
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.print_queue()

print("\nDequeue the first value")
dequeued = my_queue.dequeue()
print("Dequeued:", dequeued)
my_queue.print_queue()
