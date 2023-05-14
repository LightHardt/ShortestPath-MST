'''
File: AStar.py
Author: Matteo Bassani

Implementation of A* algorithm. This requires the data structure [GraphADT.py] 
which implementation is completely based on an adjacency matrix.
'''

# This function is called only when a new node is reached. The shortest path to get
# to it is here initialized.
def add_weight(graph,current,neighbor):
  
  # Length of the shortest path is initialized
  graph.node(neighbor).g = graph.node(current).g + graph.get_edge_data(current,neighbor)

  # Route to get to the node is initialized
  graph.node(neighbor).route.extend(graph.node(current).route)
  graph.node(neighbor).route.append(neighbor)



# This function is called to check if a better path is found to get to a node that
# has been reached before, but never visited.
def update_open_weight(graph,current,neighbor):
  
  # Best path lenght until now
  old_weight = graph.node(neighbor).g
  # New path length
  new_weight = graph.node(current).g + graph.get_edge_data(current,neighbor)

  # If we found a better path, best path is updated
  if new_weight < old_weight:
    graph.node(neighbor).g = new_weight
    graph.node(neighbor).route = (graph.node(current).route)
    graph.node(neighbor).route.append(neighbor)



# This function is called to check if a better path is found to get to a node that
# has been already been visited. If this is true, all the best paths to his neighbors
# must be updated.
def update_closed_weight(graph,current,neighbor):
  
  # Best path lenght until now
  old_weight = graph.node(neighbor).g
  # New path length
  new_weight = graph.node(current).g + graph.get_edge_data(current,neighbor)

  # If we found a better path, best path is updated
  if new_weight < old_weight:
    graph.node(neighbor).g = new_weight
    graph.node(neighbor).route = (graph.node(current).route)
    graph.node(neighbor).route.append(neighbor)
    # Every neighbor not yet visited must update his best path with the new one
    for next in graph.neighbors(neighbor):
      if not graph.node(next).visited:
        update_closed_weight(graph,neighbor,next) # Recursive call



# A Star Algorithm: find the shortest path between two nodes based on an heuristic.
def AStar(graph,start,end,heuristic,queue):
  
  if graph.isEmpty():
    return ([],0)
  if (start or end) not in graph.nodes_names():
    return ([],0)
  
  visited = []
  visiting = []
  
  # Start node is enqueued and initialized
  queue.enqueue(start,heuristic[start])
  graph.node(start).route.append(start)
  

  while not queue.is_empty():
    current = queue.dequeue()
    visited.append(current)

    if current == end:
      return graph.node(current).route, graph.node(current).g, visited, visiting
    graph.node(current).visited = True

    neighborhood = []

    for neighbor in graph.neighbors(current):
      
      if graph.node(neighbor).visited:
        update_closed_weight(graph,current,neighbor)
      else:
        neighborhood.append(neighbor)
        if queue.exists(neighbor):
          update_open_weight(graph,current,neighbor)
        else:
          add_weight(graph,current,neighbor)
          queue.enqueue(neighbor,graph.node(neighbor).g + heuristic[neighbor])

    visiting.append(neighborhood)
  return ([],0)
