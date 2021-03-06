import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It can be constructed/deconstructed in constant
        # time without needing to be rebuilt.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)
