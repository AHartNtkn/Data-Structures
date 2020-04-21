# Canonical endofunctor map
# Here, the endofunctor is modeled as a type which is either
# None, modeling an empty leaf, or a tuple consisting of
# the left tree recurse, the value, and the right tree recurse.
def bst_efmap(f, nF):
    if nF is None:
        return None
    elif isinstance(nF, BinarySearchTree):
        return BinarySearchTree(nF.value, f(nF.left), f(nF.right))

# Generic catamorphism over BSTs
def bst_cata(alg, bst):
    return alg(bst_efmap(lambda x: bst_cata(alg, x), bst))

# A generic algebra generated from an ordering
def order_alg(*order):
    fst, snd, trd = order
    def alg(trF):
      if trF is None:
          return []
      elif isinstance(trF, BinarySearchTree):
          out = (trF.left, [trF.value], trF.right)

          return out[fst] + out[snd] + out[trd]

    return alg

def in_order(tr):
    return bst_cata(order_alg(0, 1, 2), tr)

def debth_first(tr):
    return bst_cata(order_alg(1, 0, 2), tr)

def post_order(tr):
    return bst_cata(order_alg(0, 2, 1), tr)

# riffle two lists together
def riffle(l1, l2):
    m = min(len(l1), len(l2))
    return [ x for p in zip(l1, l2) for x in p ] + l1[m:] + l2[m:]

# Algebra for creating a list of items in the tree, breadth first.
def breadth_first_alg(trF):
    if trF is None:
        return []
    elif isinstance(trF, BinarySearchTree):
        return [trF.value] + riffle(trF.right, trF.left)

def breadth_first(tr):
    return bst_cata(breadth_first_alg, tr)



# Containment should be defined as a hylomorphism over lists.
# It *can* be defined as a catamorphism over BinTrees, but that
# means one deconstruction is run per constructor; not per layer.
# We need to generate a list corresponding to the trace of the
# program using a coalgebra and then collapse the list. This
# will use only one operation per list constructor, which should
# correspond to the tree's depth up to the found target.
def list_efmap(f, nF):
    if nF is None:
        return None
    elif isinstance(nF, tuple):
        return (nF[0], f(nF[1]))

def list_hylo(alg, coalg, i):
    return alg(list_efmap(lambda x: list_hylo(alg, coalg, x), coalg(i)))

def contains_alg(target):
    def go(lF):
        if lF is None:
            return False
        elif isinstance(lF, tuple):
            return lF[0] or lF[1]

    return go

def contains_coalg(target):
    def go(bst):
        if bst is None:
            return None
        else:
            if target < bst.value:
                return (False, bst.left)
            elif target == bst.value:
                return (True, None)
            else:
                return (False, bst.right)

    return go




class BinarySearchTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right    

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        return list_hylo(contains_alg(target), contains_coalg(target), self)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        self.value = cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        [ print(x) for x in in_order(self) ] 

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        [ print(x) for x in breadth_first(self) ] 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        [ print(x) for x in debth_first(self) ] 

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        [ print(x) for x in debth_first(self) ] 

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        [ print(x) for x in post_order(self) ] 
