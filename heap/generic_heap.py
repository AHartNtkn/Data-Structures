def first_child(index):
    return 2 * index + 1

def second_child(index):
    return 2 * (index + 1)

def parent(index):
    return (index + 1)//2 - 1

class Heap:
    def __init__(self, comparator = None):
        self.storage = []
        if comparator == None:
            self.comparator = lambda x, y: x > y
        else:
            self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        for i in range(len(self.storage)-1, -1, -1):
            self._bubble_up(i)

    def delete(self):
        topmost = self.storage[0]
        new_top = self.storage.pop()
        if self.storage != []:
          self.storage[0] = new_top
          for i in range(len(self.storage)):
              self._sift_down(i)
        return topmost

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index >= len(self.storage):
            return None

        if index == 0:
            return None

        parent_index = parent(index)
        if self.comparator(self.storage[index], self.storage[parent_index]):
            self.storage[parent_index], self.storage[index] =\
            self.storage[index], self.storage[parent_index]

    def _sift_down(self, index):-
        if index >= len(self.storage):
            return None

        child_1_index = first_child(index)
        if child_1_index >= len(self.storage):
            return None-

        child_2_index = second_child(index)

        if child_2_index >= len(self.storage) or\
           self.comparator(self.storage[child_1_index], self.storage[child_2_index]):
            if self.comparator(self.storage[child_1_index], self.storage[index]):
                self.storage[child_1_index], self.storage[index] =\
                self.storage[index], self.storage[child_1_index]
        else:
            if self.comparator(self.storage[child_2_index], self.storage[index]):
                self.storage[child_2_index], self.storage[index] =\
                self.storage[index], self.storage[child_2_index]
