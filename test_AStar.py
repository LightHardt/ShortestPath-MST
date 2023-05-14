'''
File: test_AStar.py
Author: Matteo Bassani

Test suite for AStar to ensure functionality
'''

import pytest
from AStar import *
from GraphADT import *
from DrawGraph import create_graph, h1
import PQLL
import PQMinHeap


class TestAStar:

    @pytest.fixture
    def graph(self):
        return GraphADT(create_graph())
    
    # testing incorrect input using PQLL
    def test_AStar_wrong_input_PQLL(self, graph):
        assert AStar(graph,"Arad","goofy",h1(),PQLL.PriorityQueueLL())[0] == []
        assert AStar(graph,"pluto","Iasi",h1(),PQLL.PriorityQueueLL())[0] == []
        assert AStar(graph,"goofy","pluto",h1(),PQLL.PriorityQueueLL())[0] == []
    
    # testing when start == end using PQLL
    def test_AStar_already_here_PQLL(self, graph):
        assert AStar(graph,"Bucharest","Bucharest",h1(),PQLL.PriorityQueueLL())[0] == ["Bucharest"]
    
    # testing sample path 1 using PQLL
    def test_AStar_path1_PQLL(self, graph):
        assert AStar(graph,"Arad", "Bucharest", h1(),PQLL.PriorityQueueLL())[0] == ["Arad", "Sibiu", "Rimnicu", "Pitesti", "Bucharest"]
    
    # testing sample path 2 using PQLL
    def test_AStar_path2_PQLL(self, graph):
        assert AStar(graph,"Oradea","Bucharest",h1(),PQLL.PriorityQueueLL())[0] == ["Oradea", "Sibiu", "Rimnicu", "Pitesti", "Bucharest"]
    
    # testing sample path 3 using PQLL
    def test_AStar_path3_PQLL(self, graph):
        assert AStar(graph,"Neamt","Bucharest",h1(),PQLL.PriorityQueueLL())[0] == ["Neamt", "Iasi", "Vaslui", "Urziceni", "Bucharest"]
    
    # testing sample path 4 using PQLL
    def test_AStar_path4_PQLL(self, graph):
        assert AStar(graph,"Lugoj","Bucharest",h1(),PQLL.PriorityQueueLL())[0] == ["Lugoj", "Mehadia", "Dobreta", "Craiova", "Pitesti", "Bucharest"]

    # testing incorrect input using PQMinHeap
    def test_AStar_wrong_input_PQMinHeap(self, graph):
        assert AStar(graph,"Arad","goofy",h1(),PQMinHeap.PQMinHeap())[0] == []
        assert AStar(graph,"pluto","Iasi",h1(),PQMinHeap.PQMinHeap())[0] == []
        assert AStar(graph,"goofy","pluto",h1(),PQMinHeap.PQMinHeap())[0] == []
    
    # testing when start == end using PQMinHeap
    def test_AStar_already_here_PQMinHeap(self, graph):
        assert AStar(graph,"Bucharest","Bucharest",h1(),PQMinHeap.PQMinHeap())[0] == ["Bucharest"]
    
    # testing sample path 1 using PQMinHeap
    def test_AStar_path1_PQMinHeap(self, graph):
        assert AStar(graph,"Arad", "Bucharest", h1(),PQMinHeap.PQMinHeap())[0] == ["Arad", "Sibiu", "Rimnicu", "Pitesti", "Bucharest"]
    
    # testing sample path 2 using PQMinHeap
    def test_AStar_path2_PQMinHeap(self, graph):
        assert AStar(graph,"Oradea","Bucharest",h1(),PQMinHeap.PQMinHeap())[0] == ["Oradea", "Sibiu", "Rimnicu", "Pitesti", "Bucharest"]
    
    # testing sample path 3 using PQMinHeap
    def test_AStar_path3_PQMinHeap(self, graph):
        assert AStar(graph,"Neamt","Bucharest",h1(),PQMinHeap.PQMinHeap())[0] == ["Neamt", "Iasi", "Vaslui", "Urziceni", "Bucharest"]
    
    # testing sample path 4 using PQMinHeap
    def test_AStar_path4_PQMinHeap(self, graph):
        assert AStar(graph,"Lugoj","Bucharest",h1(),PQMinHeap.PQMinHeap())[0] == ["Lugoj", "Mehadia", "Dobreta", "Craiova", "Pitesti", "Bucharest"]