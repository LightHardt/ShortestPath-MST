'''
File: test_GraphADT.py
Author: Matteo Bassani

Test suite for GraphADT to ensure functionality
'''
import pytest
from GraphADT import *
import networkx as nx

class TestPriorityQueueLL:

    @pytest.fixture
    def graph(self):
        graphnx=nx.Graph()
        graphnx.add_edge("A","B", weight=3)
        graphnx.add_edge("B","C", weight=2)
        return GraphADT(graphnx)

    # testing isEmpty (positive case)
    def test_empty_true(self):
        graph_empty=GraphADT(nx.Graph())
        assert graph_empty.isEmpty() == True

    # testing isEmpty (negative case)
    def test_empty_false(self,graph):
        assert graph.isEmpty() == False

    # testing node
    def test_node(self,graph):
        assert graph.node('A').name == 'A'
        assert graph.node('B').label == 1
        assert graph.node('C').route == []
        assert graph.node('A').visited == False
        assert graph.node('B').g == 0

    # testing node_at
    def test_node_at(self,graph):
        assert graph.node_at(-1) == None
        assert graph.node_at(0) == 'A'
        assert graph.node_at(1) == 'B'
        assert graph.node_at(2) == 'C'
        assert graph.node_at(3) == None

    # testing adjacent
    def test_adjacent(self,graph):
        assert graph.adjacent('A','B') == True
        assert graph.adjacent('A','C') == False
        assert graph.adjacent('B','C') == True

    # testing neighbors
    def test_neighbors(self,graph):
        assert graph.neighbors('A') == ['B']
        assert graph.neighbors('B') == ['A','C']
        assert graph.neighbors('C') == ['B']

    # testing get_edge_data
    def test_get_edge_data(self,graph):
        assert graph.get_edge_data('A','B') == 3
        assert graph.get_edge_data('A','C') == 0
        assert graph.get_edge_data('C','B') == 2

    # testing add_edge
    def test_add_edge(self,graph):
        assert graph.get_edge_data('A','C') == 0
        assert graph.get_edge_data('C','A') == 0
        graph.add_edge('A','C',4)
        assert graph.get_edge_data('A','C') == 4
        assert graph.get_edge_data('C','A') == 4

    # testing remove_edge
    def test_remove_edge(self,graph):
        assert graph.get_edge_data('A','B') == 3
        assert graph.get_edge_data('B','A') == 3
        graph.remove_edge('A','B')
        assert graph.get_edge_data('A','B') == 0
        assert graph.get_edge_data('B','A') == 0

