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
        # my_list = LinkedList("A", "2", 2, "Q")


    def __str__(self):
        '''
        Defines behavior for when str() is called on an instance of your class.
        '''
        pass

    def __len__(self):
        '''
        Returns the length of the container. Part of the protocol for both immutable and mutable containers.
        '''
        #return elements.__len__()
        #length = self.end.index()
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
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        
        #compare self.start to other.start
        # lengthsAreNotEqual = self.count() != other.count()
        # if (lengthsAreNotEqual):
        #     return False
        
        # for selfNode,otherNode in zip(self, other):
        #     if selfNode.elem != otherNode.elem:
        #         return False
        # return True
        
       
        
        # selfNode = self.start
        # otherNode = other.start
        
    
        # while (selfNode and otherNode):
        
        #     if selfNode.elem != otherNode.elem:
        #         return False
                    
        #     selfNode = selfNode.next
        #     otherNode = otherNode.next
            
        # return True
        
        listOfSelfElem = [node.elem for node in self]
        listOfOtherElem = [node.elem for node in other]
        return listOfOtherElem == listOfOtherElem
        
        
            
        
        
 

    def append(self, elem):
        temp = Node(elem)
        
        # Assuming empty linkedlist
        if self.start is None:
            self.start = temp
            self.end = self.start
        
        self.end.next = temp
        self.end = temp
        

    def count(self):
        # if self is None:
        #     return 0
        # return len(self)
        # for self.start in temp 
        return len(self)
    


    def pop(self, index=None):
        #pop_node = self.start
        # when index == None
        
        if index is None:   # user doesn't input an index
            for node in self:
                if node.next == self.end:   # if node is second-to-last-node
                    endValue = self.end.elem  # set endValue to last node's elem
                    self.end = node # change self.end to second to last node
                    self.end.next = None #change self.next to None
            
                    return endValue
                    
                    

                
        # # user does input an index
        # else:
        #     counter = 0
        #     for node in self:
        #         previousNode = node
        #         node = node.next 
        #         nextNode = node.next
                
        #         if counter == index:
        #             #connect the 2 nodes here
                    
        #             previousNode.next = nextNode
        #             return node.elem
                    
        #         counter += 1
    
            
        
            
        
        