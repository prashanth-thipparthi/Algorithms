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

time = 0
smallestCycleTime = -math.inf
startTime = 0

def depthFirstTraversal(graph,node,searchNode,cycleNodeflag,bookKeepingDict,startFlag):
    global time
    global startTime
    global smallestCycleTime
    if node == searchNode:
        if cycleNodeflag :
            newTime = time - startTime
            if newTime < smallestCycleTime:
                smallestCycleTime = newTime
            startTime = 0
            time = 0
        else:
            cycleNodeflag = True
            startTime = time
    if node in bookKeepingDict:
        if bookKeepingDict[node]["seen"]:
            return ;
        else:
            bookKeepingDict[node]["seen"] = True

    if (startFlag):
        flag = False
        bookKeepingDict[node] = {}
        bookKeepingDict[node]["parent"] = None
    bookKeepingDict[node]["discoveyTime"] = time

    for adjNode in graph[node]:
        if not adjNode in bookKeepingDict:
            bookKeepingDict[adjNode] = {}
            bookKeepingDict[adjNode]["seen"] = False
            bookKeepingDict = depthFirstTraversal(graph,adjNode,bookKeepingDict,flag)
    return bookKeepingDict


bookKeepingDict = {}
time = 0
node = 1
flag = True
print(depthFirstTraversal(graph3,node,searchNode,cycleNodeflag,bookKeepingDict,startFlag))
