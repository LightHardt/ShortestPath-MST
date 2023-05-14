'''
File: test_Prims.py
Author: Nathan Rayon

Test suite for prims algorithm to ensure functionality
'''
import pytest
from Prims import *
from GraphADT import *
from DrawGraph import create_graph
import PQLL, PQMinHeap
import networkx as nx

testGraph = nx.Graph()
testGraph.add_edge("Arad","Zerind", weight=75)
testGraph.add_edge("Zerind","Oradea", weight=71)
testGraph.add_edge("Arad","Timisoara", weight=118)
testGraph.add_edge("Timisoara","Lugoj", weight=111)
testGraph.add_edge("Lugoj","Mehadia", weight=70)
testGraph.add_edge("Mehadia","Dobreta", weight=75)
testGraph.add_edge("Dobreta","Craiova", weight=120)
testGraph.add_edge("Craiova","Pitesti", weight=138)
testGraph.add_edge("Pitesti","Rimnicu", weight=97)
testGraph.add_edge("Pitesti","Bucharest", weight=101)
testGraph.add_edge("Bucharest","Giurgiu", weight=90)
testGraph.add_edge("Rimnicu","Sibiu", weight=80)
testGraph.add_edge("Sibiu","Fagaras", weight=99)
testGraph.add_edge("Bucharest","Urziceni", weight=85)
testGraph.add_edge("Urziceni","Hirsova", weight=98)
testGraph.add_edge("Hirsova","Eforie", weight=86)
testGraph.add_edge("Urziceni","Vaslui", weight=142)
testGraph.add_edge("Vaslui","lasi", weight=92)
testGraph.add_edge("lasi","Neamt", weight=87)



class TestPrims:

    @pytest.fixture
    def graph(self):
        return GraphADT(create_graph())
    
    # testing incorrect input using PQLL
    def test_Prims_wrong_input_PQLL(self, graph):
        assert Prims(graph,"Incorrect", PQLL.PriorityQueueLL())[0] == []

    # testing incorrect input using PQMinHeap
    def test_Prims_wrong_input_PQMinHeap(self, graph):
        assert Prims(graph,"Incorrect", PQMinHeap.PQMinHeap())[0] == []

    # testing sample path using PQLL
    def test_Prims(self, graph):
        assert nx.is_isomorphic(Prims(graph,"Arad", PQLL.PriorityQueueLL())[0], testGraph)
    
    # testing sample path using PQMinHeap
    def test_AStar_path1_PQMinHeap(self, graph):
        assert nx.is_isomorphic(Prims(graph,"Arad", PQMinHeap.PQMinHeap())[0], testGraph)
    