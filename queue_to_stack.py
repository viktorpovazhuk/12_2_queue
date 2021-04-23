"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue  # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack  # or from linkedstack import LinkedStack


def queue_to_stack(queue):

    elements = []
    while not queue.isEmpty():
        elements.append(queue.pop())
    for el in elements:
        queue.add(el)
    # for i in range(-1, -(len(elements) + 1), -1):
    #     stack.push(elements[i])
    stack = ArrayStack(reversed(elements))
    return stack


if __name__ == "__main__":
    queue = ArrayQueue()
    for i in range(10):
        queue.add(i)
    stack = queue_to_stack(queue)
    print(queue)
    print(stack)
    print(stack.pop())
    print(queue.pop())
    stack.add(11)
    queue.add(11)
    print(queue)
    print(stack)
