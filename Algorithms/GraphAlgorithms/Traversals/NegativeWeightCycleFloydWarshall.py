from collections import defaultdict
import math

class Graph:

    def __init__(self):
        self.graph = defaultdict(dict)
        self.vertices = list
        self.NoOfVertices = 7
        self.pathNodes = defaultdict(dict)

    def addVertices(self, verticesList):
        self.vertices = verticesList

    def addEdge(self, u, v, w):
        # if(u in self.graph):
        if len(self.graph[u])>0:
            self.graph[u][v] = w
        else:
            self.graph[u] = {v:w}

    def updateGraph(self):
        for node in self.vertices :
            for secondaryNode in self.vertices:
                if secondaryNode in self.graph[node]:
                    continue
                else:
                    if node == secondaryNode:
                        self.graph[node][secondaryNode] = 0
                    else:
                        self.graph[node][secondaryNode] = math.inf

    def updatePathNodes(self):
        for node in self.vertices :
            for secondaryNode in self.vertices:
                if secondaryNode in self.graph[node]:
                    continue
                else:
                    if node == secondaryNode:
                        self.graph[node][secondaryNode] = secondaryNode
                    else:
                        self.graph[node][secondaryNode] = math.inf

    def floydWarshall_AllPairsShortestPath(self):
        #dist=[[0 for i in range(self.NoOfVertices+1)]for j in range(self.NoOfVertices+1)]
        dist = defaultdict(dict)

        for node in self.vertices :
            dist[node] = {}
            for secondaryNode in self.vertices:
                dist[node][secondaryNode] = 0

        for node in self.vertices :
            for secondaryNode in self.vertices:
                dist[node][secondaryNode] = self.graph[node][secondaryNode]

        for intermediateNode in self.vertices:
            for sourceNode in self.vertices:
                for destinationNode in self.vertices:
                    if (dist[sourceNode][intermediateNode] + dist[intermediateNode][destinationNode] < dist[sourceNode][destinationNode]):
                        dist[sourceNode][destinationNode] = dist[sourceNode][intermediateNode] + dist[intermediateNode][destinationNode]

        print(dist)

        for node in self.vertices:
            if (dist[node][node] < 0):
                return True

        return False



g1 = Graph()
g1.addVertices((1,2,3,4,5,6,7))
g1.addEdge(1,2,1)
g1.addEdge(1,5,4)
g1.addEdge(2,3,3)
g1.addEdge(3,4,4)
g1.addEdge(4,5,5)
g1.addEdge(3,6,-2)
g1.addEdge(6,7,4)
g1.addEdge(7,2,1)

#print(g1.graph)
g1.updateGraph()
print(g1.floydWarshall_AllPairsShortestPath())