'''
File: PQMinHeap.py
Author: Dean Golden

Implementation of Priority Queue utilizing a binary min heap
'''
import math

# Class to hold data
class Node:
    def __init__(self,name,heuristic):
        self.name = name
        self.heuristic = heuristic

# Priority queue with binary min heap
class PQMinHeap:
    def __init__(self):
        self.heap = []
    
    # Print contents of heap
    def print(self):
        for x in self.heap:
            print(x,end=' ')
        print()
    
    # Check if heap is empty
    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
    
    # Get min value without removing it
    def peek(self):
        if not self.is_empty():
            return self.heap[0].name
        return None
    
    # Determine if given element is in heap
    def exists(self,element):
        if self.is_empty():
            return False
        for x in self.heap:
            if x.name == element:
                return True
        return False
    
    # Add value to priority queue
    def enqueue(self,name,heur):
        # Add value as root
        if self.is_empty():
            self.heap.append(Node(name,heur))
            return
        
        # Add value to heap and save index
        self.heap.append(Node(name,heur))
        child_index = len(self.heap) - 1

        # Propagate up if needed
        while(child_index != 0):
            # Even indexes are right nodes and need to grab parent node via floor(index/2) - 1
            if child_index % 2 == 0:
                parent_index = math.floor((child_index/2)) - 1
                parent = self.heap[parent_index]
                # If child is smaller then parent swap
                if self.heap[child_index].heuristic < parent.heuristic:
                    self.heap[parent_index] = self.heap[child_index]
                    self.heap[child_index] = parent
                    child_index = parent_index
                else:
                    break
            # Odd indexes are left nodes and can grab parent nodes via floor(index/2)
            else:
                parent_index = math.floor(child_index / 2)
                parent = self.heap[parent_index]
                # If child is smaller then parent swap
                if self.heap[child_index].heuristic < parent.heuristic:
                    self.heap[parent_index] = self.heap[child_index]
                    self.heap[child_index] = parent
                    child_index = parent_index
                else:
                    break
    
    # Remove min from heap
    def dequeue(self):
        if self.is_empty():
            return None
        # save root to return it at end
        root = self.heap[0]
        # grab index of last value in heap
        end = len(self.heap) - 1
        # put last value in heap as root
        self.heap[0] = self.heap[end]
        # shrink heap
        self.heap.pop()
        # set index at 0 to percolate down if needed
        index = 0

        # percolate down to keep min-heap state if needed
        while(True):
            # access left leaf of a node
            left_node = (index * 2) + 1
            # access right leaf of a node
            right_node = (index * 2) + 2
            # check to make sure not checking a non existent index
            if left_node < len(self.heap) and right_node < len(self.heap):
                # compare leafs to determine smallest to swap if needed
                if self.heap[left_node].heuristic < self.heap[right_node].heuristic:
                    if self.heap[left_node].heuristic < self.heap[index].heuristic:
                        temp = self.heap[index]
                        self.heap[index] = self.heap[left_node]
                        self.heap[left_node] = temp
                        index = left_node
                    else:
                        break
                else:
                    if self.heap[right_node].heuristic < self.heap[index].heuristic:
                        temp = self.heap[index]
                        self.heap[index] = self.heap[right_node]
                        self.heap[right_node] = temp
                        index = right_node
                    else:
                        break
            # Only check the one leaf the parent node has and swap if necessary
            elif left_node < len(self.heap):
                if self.heap[left_node].heuristic < self.heap[index].heuristic:
                        temp = self.heap[index]
                        self.heap[index] = self.heap[left_node]
                        self.heap[left_node] = temp
                        index = left_node
                else:
                    break
            else:
                break
        return root.name