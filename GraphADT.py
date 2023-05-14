'''
File: GraphADT.py
Author: Matteo Bassani

Implementation of Graph Data Structure used in AStar.py.
Implemented using an adjacency matrix.
'''

import numpy as np

# The GraphNode class is the representation of one node in the graph
class GraphNode:
    def __init__(self, name, label, route, visited, g, parent):
        # Name of the node
        self.name = name 
        # Numerical label of the node in the adjacency matrix
        self.label = label
        # Shortest route to get to the node
        self.route = route 
        # Is the node already visited in the algorithm?
        self.visited = visited 
        # Lenght of the shortest path to get to the node
        self.g = g 
        # Previous node in route
        self.parent = parent
# The GraphADT class is the representation of the Graph used by A* algorithm.
# It contains several methods that allows an easier and more high level access of the graph.
class GraphADT:

    # Constructor 1: an instance of a nextworkx graph (used for GUI) 
    # is transformed in GraphADT instance
    def __init__(self, graphnx):

        # Number of nodes
        n = len(graphnx)

        # Adjacency matrix
        adj_matrix = np.zeros((n, n))

        # This dictionary contains every node in the graph. Keys are node_names (O(1) access to nodes)
        node_list = {node: GraphNode(node,i,[],False,0,"") for i, node in enumerate(graphnx.nodes())}
        
        # Adjacency matrix and node list are initialized
        for u, v, w in graphnx.edges(data="weight"):
          i, j = node_list[u].label, node_list[v].label
          adj_matrix[i, j] = adj_matrix[j, i] = w
        
        # Instance variables of this class
        self.node_list = node_list
        self.adj_matrix = adj_matrix


    # Return True when the graph doesn't contain nodes
    def isEmpty(self):
        return len(self.node_list) == 0

    # Given the name of the node, return the correspondent GraphNode object
    def node(self,elem):
        # We don't check if elem exists in graph, the method must be O(1)
        return self.node_list[elem]
    
    # Return a list with the names of all the nodes
    def nodes_names(self):
        return list(self.node_list.keys())
    
    # Given the position of a node in the adjacency matrix, return its name
    def node_at(self,pos):
        if pos<0 or pos>len(self.node_list)-1:
            return None
        return self.nodes_names()[pos]
    
    # Return true if two nodes are adjacent
    def adjacent(self,x,y):
        return (self.adj_matrix[self.node_list[x].label][self.node_list[y].label]>0)
    
    # Return a list with the names of all the nodes adjacent to a specific one
    def neighbors(self,x):
        return [self.node_at(index) for index in np.where(self.adj_matrix[self.node_list[x].label] > 0)[0]]

    # Add a new weighted edge to the graph
    def add_edge(self, x, y, w):
        self.adj_matrix[self.node_list[x].label][self.node_list[y].label] = w
        self.adj_matrix[self.node_list[y].label][self.node_list[x].label] = w

    # Remove an edge from the graph
    def remove_edge(self, x, y):
        self.adj_matrix[self.node_list[x].label][self.node_list[y].label] = 0
        self.adj_matrix[self.node_list[y].label][self.node_list[x].label] = 0
    
    # Given two nodes, return the weight of a specific edge (0 if not linked)
    def get_edge_data(self, x, y):
        return self.adj_matrix[self.node_list[x].label][self.node_list[y].label]