'''
File: test_PQMinHeap.py
Author: Dean Golden

Test suite for PQMinHeap to ensure functionality
'''
import pytest
from PQMinHeap import *

@pytest.fixture
def pq():
    return PQMinHeap()

def test_is_empty(pq: PQMinHeap):
    assert pq.is_empty() == True
    
    pq.enqueue("Dubai",1)
    assert pq.is_empty() == False

# Make sure peek shows root if value and None if not
def test_peek(pq: PQMinHeap):
    assert pq.peek() == None
    
    pq.enqueue("New York",3)
    pq.enqueue("Madison",4)
    pq.enqueue("Georgia",2)
    assert pq.peek() == "Georgia"

# Make sure exists successfully finds element and if not false
def test_exists(pq: PQMinHeap):
    assert pq.exists("Empty") == False

    pq.enqueue("Lodesman",10)
    pq.enqueue("Fiskett",100)
    pq.enqueue("Nikou",98)
    pq.enqueue("Marbest",5)
    pq.enqueue("Eudonor",73)
    pq.enqueue("Ayder",23)

    assert pq.exists("Ayder") == True
    assert pq.exists("Marbest") == True
    assert pq.exists("New York") == False

# Make sure enqueue maintains min heap status
def test_enqueue(pq: PQMinHeap):
    pq.enqueue("Lodesman",10)
    pq.enqueue("Fiskett",100)
    pq.enqueue("Nikou",98)
    pq.enqueue("Marbest",5)
    pq.enqueue("Eudonor",73)
    pq.enqueue("Ayder",23)

    assert pq.peek() == "Marbest"

# Make sure as dequeue maintain minheap status
def test_dequeue(pq: PQMinHeap):
    pq.enqueue("Lodesman",10)
    pq.enqueue("Fiskett",100)
    pq.enqueue("Nikou",98)
    pq.enqueue("Marbest",5)
    pq.enqueue("Eudonor",73)
    pq.enqueue("Ayder",23)

    assert pq.dequeue() == "Marbest"
    assert pq.dequeue() == "Lodesman"
    assert pq.dequeue() == "Ayder"
    assert pq.dequeue() == "Eudonor"
    assert pq.dequeue() == "Nikou"
    assert pq.dequeue() == "Fiskett"
    assert pq.dequeue() == None