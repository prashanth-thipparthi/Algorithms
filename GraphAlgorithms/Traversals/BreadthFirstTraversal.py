from collections import OrderedDict

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

def breadthFirstTraversal(graph1,start):
    fifoQueue = []
    parentNodes = {}#OrderedDict()
    fifoQueue.append(start)
    parentNodes[start] = {"parent":None,"depth":0}#OrderedDict([("parent",None),("depth",0)])
    while fifoQueue:

        currentNode = fifoQueue.pop(0)  #BFS
        #currentNode = fifoQueue.pop(len(fifoQueue)-1)  #DFS
        print(currentNode)
        for node in graph1[currentNode]:
            if(node not in parentNodes):
                # if parentNodes[node]:
                parentNodes[node] = {}#OrderedDict()
                parentNodes[node]["parent"] = currentNode
                parentNodes[node]["depth"] = parentNodes[currentNode]["depth"] + 1

                fifoQueue.append(node)

    return parentNodes



print(breadthFirstTraversal(graph3,1))
#print(breadthFirstTraversal(graph2,2))
#print(graph1[7])
