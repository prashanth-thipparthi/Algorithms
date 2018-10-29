from collections import defaultdict

'''
Assumptions:
The code works if the vertices,which even do not contain any edges starting from it are added to the graph 
'''
time = 0
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = list
    def addVertices(self,verticesList):
        self.vertices= verticesList
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def depthFirstTraversalUtil(self,node,bookKeepingDict):
        global time
        if bookKeepingDict[node]["seen"]:
            return
        else:
            bookKeepingDict[node]["seen"] = True
        time+=1
        bookKeepingDict[node]["discoveryTime"] = time

        for adjNode in self.graph[node]:
            if not bookKeepingDict[adjNode]["seen"]:
                bookKeepingDict[adjNode]["parent"] = node
                self.depthFirstTraversalUtil(adjNode,bookKeepingDict)
        time+=1
        bookKeepingDict[node]["finishedTime"] = time

    def depthFirstTraversal(self,startNode):
        bookKeepingDict = defaultdict(dict)
        for node in self.vertices:
            bookKeepingDict[node]["seen"] = False
        bookKeepingDict[startNode]["parent"] = None
        print(bookKeepingDict)
        self.depthFirstTraversalUtil(startNode,bookKeepingDict)
        print(bookKeepingDict)

g1 = Graph()
g1.addVertices((1,2,3,4,5))
g1.addEdge(1,2)
g1.addEdge(1,4)
g1.addEdge(2,3)
g1.addEdge(3,5)
g1.addEdge(4,2)

print(g1.depthFirstTraversal(1))
#print(g1.graph)





