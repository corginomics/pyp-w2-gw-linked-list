from .interface import AbstractLinkedList
from .node import Node



class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        '''
        Defines behavior for when str() is called on an instance of your class.
        '''
        output = [node.elem for node in self]
        return str(output)
        
    
    def __len__(self):
        '''
        Returns the length of the container. Part of the protocol for both immutable and mutable containers.
        '''
        counter = 0
        for node in self:
            counter += 1
        return counter

    def __iter__(self):
        '''
        Should return an iterator for the container. Iterators are returned in a
        number of contexts, most notably by the iter() built in function and when
        a container is looped over using the form for x in container:. Iterators
        are their own objects, and they also must define an __iter__ method that
        returns self.
        '''
        node = self.start

        while node:
            yield node
            node = node.next
        raise StopIteration
        
    def __getitem__(self, index):
        if index is None:
            raise KeyError
        if not isinstance(index, int):
            raise TypeError()
        if index >= len(self):
            raise IndexError()
            
        counter = 0
        for node in self:
            if counter == index:
                return node.elem
            counter += 1

    def __add__(self, other):
        
        newList = self.__class__()
        
        for node in self:
            newList.append(node.elem)
        for node in other:
            newList.append(node.elem)
        return newList

    def __iadd__(self, other):
        for node in other:
            self.append(node.elem)
        return self
            
        # failing on self is None and other has 2 nodes

    def __eq__(self, other):
        # do we need to take 
        # Test for self and other being empty
        if self is None and other is None:
            return True
            
        # Test for one or the other is empty, but not both (XOR)
        if (self is None and other is not None) or (self is not None and other is None):
            return False
            
        selfNode = self.start
        otherNode = other.start
        
        while (selfNode != self.end and otherNode != other.end):
            if selfNode.elem != otherNode.elem:
                return False
            selfNode = selfNode.next
            otherNode = otherNode.next
        return True
    
    def __ne__(self, other):
        if self is not other:
            return True

    def append(self, elem):
        temp = Node(elem)
        linkedListIsEmpty = self.start is None
        if linkedListIsEmpty:
            self.start = temp
            self.end = self.start
        else: 
            self.end.next = temp
            self.end = temp
        

    def count(self):
        # if self is None:
        #     return 0
        # return len(self)
        # for self.start in temp 
        return len(self)
    


    def pop(self, index=None):
        
        # Raise error if linkedlist is empty
        if len(self) == 0:
            raise IndexError()
        
        # Raise error if index is greater than or equal to index
        if index is not None:
            if index >= len(self) or index < 0:
                raise IndexError()
        
        #popping the end, or when index=None
        if index is None or (len(self) - 1 == index):
            for node in self:
                if node.next == self.end:   # if node is second-to-last-node
                    endValue = self.end.elem  # set endValue to last node's elem
                    self.end = node # change self.end to second to last node
                    self.end.next = None #change self.next to None
                    return endValue
        
        #pop from beginning, user enters index=0, or when ___________
        if index == 0 or len(self) == 1:
            linkedListLengthGreaterThanOne = len(self) != 1
            importantValue = self.start.elem
            
            if (linkedListLengthGreaterThanOne):   
                nodeAhead = self.start.next
                self.start = nodeAhead
            else:
                self.start = None
                self.end = None
        
            return importantValue
    
        #poppping from the middl
        counter = 0
        for node in self:
            # if nextNode == None:
            #     break
            previousNode = node
            node = node.next
            nextNode = node.next
            counter += 1
            
            if (counter == index):
                importantValue = node.elem
                previousNode.next = nextNode
                return importantValue
            
        