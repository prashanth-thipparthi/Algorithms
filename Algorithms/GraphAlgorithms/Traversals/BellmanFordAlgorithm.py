from collections import OrderedDict
import math

graph1 = OrderedDict()

graph1[1] =[2,4]
graph1[2] = [1,3]
graph1[3] = [2,4,6]
graph1[4] = [1,3,5]
graph1[5] = [4,6,7]
graph1[6] = [3,5]
graph1[7] = [5]

graph2 = OrderedDict()

graph2[0] = [1,2]
graph2[1] = [0,2,3]
graph2[2] = [0,1,3]
graph2[3] = [2,1]

graph3 = {}#OrderedDict()
graph3[1] = [2,3]
graph3[2] = [4]
graph3[3] = [4]
graph3[4] = []

graphGeeksForGeeks = {
    "A":{"B":-1,"C":4},
    "B":{"C":3,"D":2,"E":2},
    "C":{},
    "D":{"B":1,"C":5},
    "E":{"D":-3}}

def relaxOperationOnEdge(graph,bookKeepingTable,node,edgeNode):
    return bookKeepingTable[node]["cost"] + graph[node][edgeNode]

def bellmanFord(graph,start):
    bookKeepingTable = {}

    # Step 1: Initialize distances from src to all other vertices
    # as INFINITE
    for node in graph:
        bookKeepingTable[node] = {}
        bookKeepingTable[node]["cost"] = math.inf
        bookKeepingTable[node]["parent"] = None
    bookKeepingTable[start]["cost"] = 0

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for i in range(0,len(graph)-2):
        for node in graph:
            for edgeNode in graph[node]:
                x = relaxOperationOnEdge(graph,bookKeepingTable,node,edgeNode)
                if x < bookKeepingTable[edgeNode]["cost"]:
                    bookKeepingTable[edgeNode]["parent"] = node
                    bookKeepingTable[edgeNode]["cost"] = x

    # Step 3: check for negative-weight cycles.  The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle.  If we get a shorter path, then there
    # is a cycle.
    for node in graph:
        for edgeNode in graph[node]:
            x = relaxOperationOnEdge(graph, bookKeepingTable, node, edgeNode)
            if x < bookKeepingTable[edgeNode]["cost"]:
                print("Grapgh contains negative weight cycle")
                return
    return bookKeepingTable

print(bellmanFord(graphGeeksForGeeks,"A"))