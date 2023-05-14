'''
File: DrawGraph.py
Authors: Matteo Bassani, Dean Golden, Rocio Krebs, Nathan Rayon

Implementation of GUI to show algorithm progress on network
'''
import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.animation import FuncAnimation

from GraphADT import GraphADT
import PQMinHeap, PQLL
from tkinter import messagebox
import time
import random
import math
import AStar
import Prims
import PQMinHeap
import PQLL

# Return the romanian map graph
# Author: Matteo Bassani
graph=nx.Graph()
def create_graph():
    graph.add_edge("Arad","Zerind", weight=75)
    graph.add_edge("Arad","Timisoara", weight=118)
    graph.add_edge("Arad","Sibiu", weight=140)
    graph.add_edge("Zerind","Oradea", weight=71)
    graph.add_edge("Mehadia","Lugoj", weight=70)
    graph.add_edge("Mehadia","Dobreta", weight=75)
    graph.add_edge("Craiova","Dobreta", weight=120)
    graph.add_edge("Craiova","Rimnicu", weight=146)
    graph.add_edge("Craiova","Pitesti", weight=138)
    graph.add_edge("Pitesti","Rimnicu", weight=97)
    graph.add_edge("Pitesti","Bucharest", weight=101)
    graph.add_edge("Timisoara","Lugoj", weight=111)
    graph.add_edge("Sibiu","Fagaras", weight=99)
    graph.add_edge("Bucharest","Fagaras", weight=211)
    graph.add_edge("Bucharest","Giurgiu", weight=90)
    graph.add_edge("Bucharest","Urziceni", weight=85)
    graph.add_edge("Vaslui","Urziceni", weight=142)
    graph.add_edge("Vaslui","Iasi", weight=92)
    graph.add_edge("Neamt","Iasi", weight=87)
    graph.add_edge("Hirsova","Urziceni", weight=98)
    graph.add_edge("Hirsova","Eforie", weight=86)
    graph.add_edge("Sibiu","Rimnicu", weight=80)
    graph.add_edge("Sibiu","Oradea", weight=151)
    return graph

# Return a dictionary with the corresponding heuristic. In this case the heuristic 
# is the streight-line distance from every node to Bucharest.
# Author: Matteo Bassani
def h1():
	dict={}
	dict["Bucharest"] = 0
	dict["Giurgiu"] = 77
	dict["Urziceni"] = 80
	dict["Hirsova"] = 151
	dict["Eforie"] = 161
	dict["Neamt"] = 234
	dict["Oradea"] = 380
	dict["Zerind"] = 374
	dict["Arad"] = 366
	dict["Timisoara"] = 329
	dict["Lugoj"] = 244
	dict["Mehadia"] = 241
	dict["Dobreta"] = 242
	dict["Craiova"] = 160
	dict["Sibiu"] = 253
	dict["Fagaras"] = 176
	dict["Pitesti"] = 100
	dict["Rimnicu"] = 193
	dict["Vaslui"] = 199
	dict["Iasi"] = 226
	return dict

# Author: Matteo Bassani
def update(t, nodes, order, explored, closed_nodes, final_path):
  nc = {node: [0.9,0.9,0.9] for node in closed_nodes.keys()}
  if t < len(order):
    for node in closed_nodes.keys():
      nc[node] = state_to_color(0)
      if closed_nodes[node]:
        nc[node] = state_to_color(1)
      if node==order[t] and explored[t]:
        nc[node] = state_to_color(1)
        closed_nodes[node] = True
      elif node==order[t] and not explored[t]:
        nc[node] = state_to_color(2)
  else:
    for node in final_path:
      nc[node] = state_to_color(3)
  nodes.set_color(nc.values())
  return nodes,

# Author: Matteo Bassani
def state_to_color(s):
  if s==0:
    return [0.9,0.9,0.9] #unvisited
  if s==1:
    return [0.5,0.5,1] #visited
  if s==2:
    return [1,0.5,0.5] #visiting
  return [0.5,1,0.5] #final path

# Author: Matteo Bassani
#
# Modifications: Dean Golden
def on_astar_click():

    # Check if the grid size argument is correct
    start = citychoosen.get()
    priority_queue_choice = [PQMinHeap.PQMinHeap(),PQLL.PriorityQueueLL()]
    
    graphnx = create_graph()
    result = AStar.AStar(GraphADT(graphnx), start, "Bucharest", h1(), priority_queue_choice[pq_choose.current()])

    visited = result[2]
    visiting = result[3]
    result = result[0:1]

    n = len(graphnx)
    nc = [[0.9,0.9,0.9]]*n #node color
    pos = nx.spring_layout(graphnx, seed=10)
    
    fig=plt.figure(figsize=(8,8))
    nodes = nx.draw_networkx_nodes(graphnx,pos,node_color=nc,node_size=400) #layout of nodes
    nx.draw_networkx_edges(graphnx,pos) #layout of edges
    nx.draw_networkx_labels(graphnx, pos, font_size=12, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(graphnx, "weight")
    nx.draw_networkx_edge_labels(graphnx, pos, edge_labels)

    visiting.append([])
    order = []
    explored = []
    for i in range(len(visited)):
      order.append(visited[i])
      explored.append(True)
      for neighbor in visiting[i]:
        order.append(neighbor)
        explored.append(False)
  
    closed_nodes = {node: False for node in graphnx.nodes()}
    anim = FuncAnimation(fig, update, fargs = (nodes, order, explored, closed_nodes, result[0]), interval=400, save_count=len(order)+1, blit=True)
    plt.show()
    rc('animation', html='jshtml')
    anim
    plt.close()

# Author: Nathan Rayon
#
# Modifications: Rocio Krebs, Dean Golden
def on_prims_click():
    #Draws the graph and displays prims visualization
    start = citychoosen.get()
    priority_queue_choice = [PQMinHeap.PQMinHeap(),PQLL.PriorityQueueLL()]
    graphnx = create_graph()

    result = Prims.Prims(GraphADT(graphnx), start, priority_queue_choice[pq_choose.current()])

    adjNodes = result[1]
    chosenNodes = result[2]

    order = []
    explored = []
  
    for node in chosenNodes:
      order.append(node)
      explored.append(True)
      for adjNode in adjNodes.pop(0):
        order.append(adjNode)
        explored.append(False)

    closed_nodes = {node: False for node in graphnx.nodes()}

    n = len(graphnx)
    nc = [[0.9,0.9,0.9]]*n #node color
    pos = nx.spring_layout(graphnx, seed=10)

    fig=plt.figure(figsize=(8,8))
    nx.draw_networkx_nodes(graphnx,pos,node_color=nc,node_size=400) #layout of nodes
    nx.draw_networkx_edges(graphnx,pos, edge_color="lightgray") #layout of edges
    nx.draw_networkx_labels(graphnx, pos, font_size=12, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(graphnx, "weight")
    nx.draw_networkx_edge_labels(graphnx, pos, edge_labels)
    final_edges = nx.draw_networkx_edges(result[0],pos)

    anim = FuncAnimation(fig, update, fargs = (final_edges, order, explored, closed_nodes, result[0]), interval=400, save_count=len(order)+1, blit=True)

    rc('animation', html='jshtml')
    anim
    plt.show()

# Author: Rocio Krebs
def add_edge(start_city, end_city, new_weight):
    ''' Add or update usder defined edge'''
    edge_description = f"Edge from {start_city} to {end_city}"
    if graph.has_edge(start_city, end_city):
        message = f"{edge_description} is updated"
        title = "Edge Updated"
    else:
        message = f"{edge_description} is added"
        title = "Edge Added"
    messagebox.showinfo(title=title, message=message)
    graph.add_edge(start_city, end_city, weight=new_weight)

# Author: Rocio Krebs
def on_add_Edge_click(): 
    ''' create a new window for options to add new edge'''
    def check_input():
      ''' check input and display a messagebox if input is not a positive integer '''
      try:
          new_weight = int(user_input.get())
          if new_weight > 0:
            add_edge(start_city.get(), end_city.get(),new_weight)
            new_window.destroy()
          else:
             messagebox.showerror(title="Input Error", message="Please enter only a positive integer")
      except ValueError:
         messagebox.showerror(title="Input Error", message="Please enter a positive integer")

    # create new Wndow
    new_window = tk.Toplevel(root)
    new_window.title("Add new edge")
 
    # create widgets
    start = tk.Label(new_window, text ='Select Start City ', font = "50") 
    start_city = ttk.Combobox(new_window, width = 10, state='readonly')
    start_city.set('Arad')  
    # Adding combobox drop down list
    start_city['values'] = ('Arad','Bucharest','Craiova','Dobreta','Eforie','Fagaras','Giurgiu', 
                        'Hirsova','Iasi','Lugoj', 'Mehadia', 'Neamt','Oradea','Pitesti',
                        'Rimnicu','Sibiu','Timisoara','Urziceni','Vaslui','Zerind')
    
    destination= tk.Label(new_window, text ='Select Destination City ', font = "50") 
    end_city = ttk.Combobox(new_window, width = 10, state='readonly')
    end_city.set('Craiova')
     # Adding combobox drop down list
    end_city['values'] = ('Arad','Bucharest','Craiova','Dobreta','Eforie','Fagaras','Giurgiu', 
                        'Hirsova','Iasi','Lugoj', 'Mehadia', 'Neamt','Oradea','Pitesti',
                        'Rimnicu','Sibiu','Timisoara','Urziceni','Vaslui','Zerind')
    weight= tk.Label(new_window, text ='Enter weight: ', font = "50")
    user_input = tk.Entry(new_window) 
    enter_button = tk.Button(new_window, text = "Enter", fg = "green", command=check_input)

    # pack widgets
    start.pack(side=tk.LEFT)
    start_city.pack(side=tk.LEFT)
    destination.pack(side=tk.LEFT)
    end_city.pack(side=tk.LEFT)
    weight.pack(side=tk.LEFT)
    user_input.pack(side=tk.LEFT)
    enter_button.pack( side = tk.LEFT)

# Author: Dean Golden
def run_benchmark():
    size = size_choose_benchmark.get()
    queue_choice = pq_choose_benchmark.current()
    num_runs = int(num_runs_choose_benchmark.get())

    priority_queue_choice = [PQMinHeap.PQMinHeap(),PQLL.PriorityQueueLL()]
    a_times = []
    p_times = []

    if size.isnumeric():
        node_size = int(size)
    elif size == 'Small':
       node_size = 50
    elif size == 'Standard':
       node_size = 200
    elif size == 'Large':
       node_size = 400
    else:
       node_size = 1000
    
    nano_to_seconds = 10**-9
    
    # Setting edges and heuristic are computationally expensive
    # generate a graph p = ln(n)/n + ln(n)/3n this helps ensure (doesnt guarantee)
    # a connected graph with most nodes containing more than one edge
    p = (math.log(node_size) / node_size) + ((math.log(node_size) / float(node_size)) / 3.0)
    graph: nx.Graph = nx.erdos_renyi_graph(node_size,p)

    # set random weights in the graph
    nx.set_edge_attributes(graph, {edge: {'weight': int(random.random() * 100) + 1} for edge in graph.edges})
    
    # assign heuristic val bases on node connectivity to target
    heuristic = {}
    for node in graph.nodes:
        if node == node_size - 1:
            heuristic[node] = 0
        else:
            heuristic[node] = nx.algorithms.approximation.local_node_connectivity(graph,node,node_size-1)
    
    # Run each for specified number of runs
    for _ in range(0,num_runs):
       begin = time.perf_counter_ns()
       AStar.AStar(GraphADT(graph),start=0,end=(node_size - 1),heuristic=heuristic,queue=priority_queue_choice[queue_choice])
       end = time.perf_counter_ns()
       a_times.append((end - begin) * nano_to_seconds)
    for _ in range(0,num_runs):
       begin = time.perf_counter_ns()
       Prims.Prims(GraphADT(graph),start=math.floor(node_size/2),queue=priority_queue_choice[queue_choice])
       end = time.perf_counter_ns()
       p_times.append((end - begin) * nano_to_seconds)
    
    if queue_choice == 0:
       title = "PQ: Min Heap Nodes: " + str(node_size)
    else:
       title = "PQ: Linked List Nodes: " + str(node_size)

    fig, ax = plt.subplots()
    ax.plot(range(0,len(a_times)),a_times,color='red')
    ax.plot(range(0,len(p_times)),p_times,color='blue')
    ax.legend(['AStar','Prim'])
    ax.set_ylabel('Seconds')
    ax.set_xlabel('Runs')
    ax.set_title(title)
    plt.show()
    return

pq_choose_benchmark: ttk.Combobox
size_choose_benchmark: ttk.Combobox
num_runs_choose_benchmark: ttk.Combobox

# Author: Dean Golden
def on_benchmark_click():
    root_benchmark = tk.Tk()
    root_benchmark.wm_title("Benchmark")
    root_benchmark.wm_protocol('WM_DELETE_WINDOW', root_benchmark.quit())

    frame_benchmark = tk.Frame(root_benchmark)
    frame_benchmark.pack(side=tk.LEFT)

    pq_benchmark = tk.Label(frame_benchmark, text="Priority Queue", font=50)
    pq_benchmark.pack(side=tk.LEFT)
    global pq_choose_benchmark 
    pq_choose_benchmark= ttk.Combobox(frame_benchmark, width = 10, state='readonly')
    pq_choose_benchmark.set("Min Heap")
    pq_choose_benchmark['values'] = ("Min Heap","Linked List")
    pq_choose_benchmark.pack(side=tk.LEFT)

    size_benchmark = tk.Label(frame_benchmark, text="Size", font=50)
    size_benchmark.pack(side=tk.LEFT)
    global size_choose_benchmark 
    size_choose_benchmark= ttk.Combobox(frame_benchmark, width = 10)
    size_choose_benchmark.set("Small")
    size_choose_benchmark['values'] = ("Small","Standard","Large",'Massive(Be careful)')
    size_choose_benchmark.pack(side=tk.LEFT)

    num_runs_benchmark = tk.Label(frame_benchmark, text="Runs", font=50)
    num_runs_benchmark.pack(side=tk.LEFT)
    global num_runs_choose_benchmark 
    num_runs_choose_benchmark = ttk.Combobox(frame_benchmark, width = 10)
    num_runs_choose_benchmark.set(50)
    num_runs_choose_benchmark['values'] = (50,100,200,500,1000)
    num_runs_choose_benchmark.pack(side=tk.LEFT)

    b1_button_benchmark = tk.Button(frame_benchmark, text ="Run", fg ="black",width=10,command=run_benchmark)
    b1_button_benchmark.pack(side = tk.LEFT)

    root_benchmark.mainloop()

    return   
   
if __name__ == "__main__":

  root = tk.Tk()
  root.wm_title("Graph")
  root.wm_protocol('WM_DELETE_WINDOW', root.quit())

  # create widgets
  w = tk.Label(root, text ='Select Start City', font = "50") 
  citychoosen = ttk.Combobox(root, width = 10, state='readonly')
  citychoosen.set('Arad')
  # Adding combobox drop down list
  citychoosen['values'] = ('Arad','Bucharest','Craiova','Dobreta','Eforie','Fagaras','Giurgiu', 
                          'Hirsova','Iasi','Lugoj', 'Mehadia', 'Neamt','Oradea','Pitesti',
                          'Rimnicu','Sibiu','Timisoara','Urziceni','Vaslui','Zerind')
  pq = tk.Label(root, text="Priority Queue", font=50)
  pq_choose = ttk.Combobox(root, width = 10, state='readonly')
  pq_choose.set("Min Heap")
  pq_choose['values'] = ("Min Heap","Linked List")
  frame = tk.Frame(root)
  bottomframe = tk.Frame(root)
  b1_button = tk.Button(frame, text ="A*", fg ="red", command=on_astar_click)
  b2_button = tk.Button(frame, text = "Prims", fg = "brown", command=on_prims_click)
  b3_button = tk.Button(frame, text = "Add Edge", fg = "green", command=on_add_Edge_click)
  b4_button = tk.Button(frame, text = "Benchmark", fg = "black", command=on_benchmark_click)

  #pack widges
  w.pack(side=tk.LEFT)
  citychoosen.pack(side=tk.LEFT)
  pq.pack(side=tk.LEFT)
  pq_choose.pack(side=tk.LEFT)
  frame.pack(side=tk.LEFT)
  bottomframe.pack( side = tk.BOTTOM )
  b1_button.pack( side = tk.LEFT)
  b2_button.pack(side = tk.LEFT)
  b3_button.pack(side = tk.LEFT)
  b4_button.pack(side = tk.LEFT)

  root.mainloop()
