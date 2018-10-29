from collections import OrderedDict
from collections import defaultdict

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

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = list

    def addVertices(self, verticesList):
        self.vertices = verticesList

    def addEdge(self, u, v):
        self.graph[u].append(v)

    #def breadthFirstTraversal_Util(graph1, start):

    def breadthFirstTraversal(self,start):
        fifoQueue = []
        parentNodes = {}#OrderedDict()
        fifoQueue.append(start)
        parentNodes[start] = {"parent":None,"depth":0}#OrderedDict([("parent",None),("depth",0)])
        while fifoQueue:
            currentNode = fifoQueue.pop(0)  #BFS
            #currentNode = fifoQueue.pop(len(fifoQueue)-1)  #DFS
            print(currentNode)
            for node in self.graph[currentNode]:
                if(node not in parentNodes):
                    # if parentNodes[node]:
                    parentNodes[node] = {}#OrderedDict()
                    parentNodes[node]["parent"] = currentNode
                    parentNodes[node]["depth"] = parentNodes[currentNode]["depth"] + 1
                    fifoQueue.append(node)
                else:
                    if node == start:
                        return True,parentNodes[currentNode]["depth"]


        return False


g1 = Graph()

g1 = Graph()
g1.addVertices((1,2,3,4,5,11,6,7,8,9,10))
g1.addEdge(1,2)
g1.addEdge(1,4)
g1.addEdge(2,3)
g1.addEdge(3,2) ##
g1.addEdge(3,5)
g1.addEdge(5,4)

g1.addEdge(4,2)

g1.addEdge(2,6)
g1.addEdge(6,7)
g1.addEdge(7,8)
g1.addEdge(8,9)
g1.addEdge(9,10)
g1.addEdge(10,2)
print(g1.breadthFirstTraversal(2))
#print(breadthFirstTraversal(graph2,2))
#print(graph1[7])
