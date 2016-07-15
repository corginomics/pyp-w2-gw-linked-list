class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


    def __str__(self):
        return str(self.elem)
    

    def __eq__(self, other):
        if self is None or other is None:
            return False
        return self.elem == other.elem

    
    def __repr__(self):
        return str(self)