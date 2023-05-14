'''
File: PQLL.py
Author: Rocio Krebs

Implementation of Priority Queue utilizing a linked list
'''
class Node:
    '''class to represent each element in the queue'''
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None
    def get_value(self):
        '''function to return value of node'''
        return self.value
    def get_priority(self):
        ''' function returns priority of node'''
        return self.priority

class PriorityQueueLL:
    '''Class implementing priority queue functionaity'''
    def __init__(self):
        self.head = None

    def is_empty(self):
        '''check if queue empy'''
        return self.head is None
    
    def enqueue(self, value, priority):
        ''' Function for adding '''
        new_node = Node(value, priority)
        if self.is_empty() or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None and priority >= current_node.next.priority:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def dequeue(self):
        ''' Funtion to remove and return element with highst priority'''
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        return value
    
    def peek(self):
        '''Function to return the element with highst priority'''
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.head.value
    
    def exists(self, elem):
        '''check if element exist in the queue'''
        current = self.head
        while current is not None:
            if current.value == elem:
                return True
            current = current.next
        return False
    
    def print_priority_queue(self):
        ''' print all elements of queue'''
        if self.is_empty():
            print("Priority queue is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next
