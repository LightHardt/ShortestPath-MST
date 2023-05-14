'''
File: Prims.py
Author: Nathan Rayon    

Implementation of Prims Algorithm using an adjacency matrix
'''

import numpy as np
import networkx as nx

def Prims(graph, start, queue):

    if graph.isEmpty():
        return ([], 0)
    if start not in graph.nodes_names():
        return ([], 0)

    MST = nx.Graph()
    for node in graph.nodes_names():
        MST.add_node(node)

    queue.enqueue(start, 0)
    currentNode = queue.dequeue()

    #AdjNodesOfCurrent and chosenNodes are for visualization purposes
    adjNodesOfCurrent = []
    chosenNodes = []
    
    adjNodes = []
    #End Loop once number of edges equal the number of vertex - 1
    while(not queue.is_empty() or currentNode == start):

        chosenNodes.append(currentNode)
        graph.node(currentNode).visited = True

        #Loop through current nodes neighbors and add nodes to queue
        for adjNode in graph.neighbors(currentNode):
            if(not graph.node(adjNode).visited):
                adjNodes.append(adjNode)
                #Set the parent node to new neighbor if the weighted edge is less than the current edge
                if graph.node(adjNode).parent == "" or graph.get_edge_data(adjNode, graph.node(adjNode).parent) > graph.get_edge_data(currentNode, adjNode): 
                    graph.node(adjNode).parent = currentNode
                
                queue.enqueue(adjNode, graph.get_edge_data(currentNode, adjNode))
        
        #Add adjnodes to list of adj nodes for visualization
        adjNodesOfCurrent.append(adjNodes)
        adjNodes = []

        #Get next edge off priority queue
        currentNode = queue.dequeue()

        #Set edge in MST
        if graph.node(currentNode).parent != "":
            MST.add_edge(graph.node(currentNode).parent, currentNode, weight=graph.get_edge_data(graph.node(currentNode).parent, currentNode))


    #Add Adj nodes of last node chosen to be none
    adjNodesOfCurrent.append([])
    
    return [MST, adjNodesOfCurrent, chosenNodes]
