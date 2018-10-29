from collections import defaultdict
import math
'''
Assumptions:
The code works if the vertices,which even do not contain any edges starting from it are added to the graph 
'''
time = 0
startTime = 0
minimunCycleTime = math.inf
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = list
    def addVertices(self,verticesList):
        self.vertices= verticesList
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def depthFirstTraversalUtil(self,node,cycleNode,bookKeepingDict,flag):
        global time
        global startTime
        global minimunCycleTime
        if bookKeepingDict[node]["seen"]:
            return
        else:
            bookKeepingDict[node]["seen"] = True
        time+=1

        for adjNode in self.graph[node]:
            if not bookKeepingDict[adjNode]["seen"]:
                self.depthFirstTraversalUtil(adjNode,cycleNode,bookKeepingDict,flag)
            else:
                if adjNode == cycleNode and bookKeepingDict[adjNode]["seen"]:
                    flag  = True
                    cycleTime = time - startTime
                    if minimunCycleTime > cycleTime:
                        minimunCycleTime = cycleTime
                    startTime = 0
                    time = 0
        time+=1

    def depthFirstTraversal(self,startNode):
        bookKeepingDict = defaultdict(dict)
        flag = False
        for node in self.vertices:
            bookKeepingDict[node]["seen"] = False
        print(bookKeepingDict)
        cycleNode = 2
        self.depthFirstTraversalUtil(cycleNode,cycleNode,bookKeepingDict,flag)
        print(bookKeepingDict)

g1 = Graph()
g1.addVertices((1,2,3,4,5,11,6,7,8,9,10))
g1.addEdge(1,2)
g1.addEdge(1,4)
g1.addEdge(2,3)
g1.addEdge(3,2) ##
g1.addEdge(3,5)
g1.addEdge(5,4)
#
g1.addEdge(3,2)
##
#g1.addEdge(4,2)
##
g1.addEdge(3,11)
#g1.addEdge(11,2)

##
g1.addEdge(2,6)
g1.addEdge(6,7)
g1.addEdge(7,8)
g1.addEdge(8,9)
g1.addEdge(9,10)
g1.addEdge(10,2)


print(g1.depthFirstTraversal(1))
print(minimunCycleTime)
#print(g1.graph)





