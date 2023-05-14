'''
File: test_priority_queueLL.py
Author: Rocio Krebs
Unit tests for PriorityQueueLL class.
'''
import sys
from io import StringIO
import pytest
from PQLL import PriorityQueueLL

class TestPriorityQueueLL:
    '''Class to test the functionality 
    of priority queue using linkedList'''

    @pytest.fixture
    def priority_queue(self):
        '''onstructor'''
        return PriorityQueueLL()

    def test_is_empty(self,priority_queue: PriorityQueueLL):
        '''Test if function recognizes content of queue'''
        assert priority_queue.is_empty() is True
        priority_queue.enqueue("task", 2)
        assert priority_queue.is_empty() is False
        priority_queue.dequeue()
        assert priority_queue.is_empty() is True
        
    def test_enqueue(self,priority_queue: PriorityQueueLL):
        '''Testing if function is adding nodes correctly'''
        priority_queue.enqueue('Node1', 1)
        priority_queue.enqueue('Node3', 3)
        priority_queue.enqueue('Node2', 2)
        assert priority_queue.peek() == 'Node1'

    def test_dequeue(self,priority_queue: PriorityQueueLL):
        '''Testing if function dequeue in right order'''
        priority_queue.enqueue('Node1', 1)
        priority_queue.enqueue('Node3', 3)
        priority_queue.enqueue('Node2', 2)
        assert priority_queue.dequeue() == 'Node1'
        assert priority_queue.dequeue() == 'Node2'
        assert priority_queue.dequeue() == 'Node3'
        assert priority_queue.dequeue() is  None

    def test_peek(self, priority_queue: PriorityQueueLL):
        '''Test if functio peek is printing the node with highest priority'''
        with pytest.raises(ValueError):
            priority_queue.peek()
        priority_queue.enqueue('Node1', 1)
        priority_queue.enqueue('Node3', 3)
        assert priority_queue.peek() == 'Node1'

    def test_exists(self, priority_queue: PriorityQueueLL):
        '''Test if node exists or no in the queue'''
        priority_queue.enqueue('Node1', 1)
        priority_queue.enqueue('Node3', 3)
        priority_queue.enqueue('Node2', 2)
        assert priority_queue.exists('Node1') is True
        assert priority_queue.exists('Node4') is False
    
    def test_print_priority_queue_empty(self, priority_queue: PriorityQueueLL):
        '''Test to see error handing when empty queue is printed'''
        output = StringIO()
        sys.stdout = output
        priority_queue.print_priority_queue()
        sys.stdout = sys.__stdout__
        captured = output.getvalue()
        assert captured == "Priority queue is empty\n"
    
    def test_print_priority_queue(self, priority_queue: PriorityQueueLL):
        '''Test if nodes are printed correctly'''
        priority_queue.enqueue('Node1', 1)
        priority_queue.enqueue('Node3', 3)
        priority_queue.enqueue('Node2', 2)
        output = StringIO()
        sys.stdout = output
        priority_queue.print_priority_queue()
        sys.stdout = sys.__stdout__
        captured = output.getvalue()
        assert captured == "Node1\nNode2\nNode3\n"

    def test_delete_empty_queue(self, priority_queue: PriorityQueueLL):
        '''delete an empty queue'''
        with pytest.raises(Exception):
            priority_queue.delete()