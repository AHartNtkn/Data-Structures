"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev

    def __str__(self):
        return str(self.value) + " :: " + str(self.next)

    
    def str_forward(self):
        if self.prev is None:
            return str(self.value)
        else:
            return self.prev.str_forward() + " :: " + str(self.value)

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head == None:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head == None:
            return None
        else:
            val = self.head.value
            self.delete(self.head)
            return val

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail == None:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail == None:
            return None
        else:
            val = self.tail.value
            self.delete(self.tail)
            return val

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node is self.head:
           self.head = node.next
        if node is self.tail:
           self.tail = node.prev
        node.delete()
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head == None:
          return None
        curnode = self.head
        curmax = self.head.value
        while curnode is not None:
            if curnode.value > curmax:
                curmax = curnode.value
            curnode = curnode.next
        return curmax

    def get(self, index):
        node = self.head
        for i in range(index):
            if node is not None:
                node = node.next
        return node
