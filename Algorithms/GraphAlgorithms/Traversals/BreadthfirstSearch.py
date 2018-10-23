from collections import OrderedDict

graph = OrderedDict()

graph[1] =(2,4)
graph[2] = (1,3)
graph[3] = (2,4,6)
graph[4] = (1,3,5)
graph[5] = (4,6,7)
graph[6] = (3,5)
graph[7] = (5)

def breadthFirstSearch(graph,start):
    pass

breadthFirstSearch(graph,1)