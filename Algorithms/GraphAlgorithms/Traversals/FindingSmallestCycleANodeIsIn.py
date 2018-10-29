from collections import OrderedDict
import math

time = 1
smallestCycleTime = math.inf
startTime = 1

def depthFirstTraversal(graph,node,cycleNode,cycleNodeFlag,bookKeepingDict,startFlag):
    global time
    global startTime
    global smallestCycleTime
    print("inside function, cycleNodeFlag", cycleNodeFlag)


    if node in bookKeepingDict:
        if bookKeepingDict[node]["seen"]:
            return ;
        else:
            bookKeepingDict[node]["seen"] = True
    time+=1
    if(startFlag):
        startFlag = False
        bookKeepingDict[node] = {}
        bookKeepingDict[node]["parent"] = None
    bookKeepingDict[node]["discoveyTime"] = time

    for adjNode in graph[node]:
        if not adjNode in bookKeepingDict:
            if node == cycleNode:
                cycleNodeFlag = True
                startTime = time
            bookKeepingDict[adjNode] = {}
            bookKeepingDict[adjNode]["seen"] = False
            bookKeepingDict[adjNode]["parent"] = node
            bookKeepingDict,cycleNodeFlag = depthFirstTraversal(graph,adjNode,cycleNode,cycleNodeFlag,bookKeepingDict,startFlag)

        else:
            if adjNode == cycleNode and cycleNodeFlag:
                newTime = time - startTime
                if newTime < smallestCycleTime:
                    smallestCycleTime = newTime
                startTime = 1
                time = 1


    time+=1
    bookKeepingDict[node]["finishTime"] = time
    return bookKeepingDict,cycleNodeFlag

graphWithCycle = {}#OrderedDict()
graphWithCycle[1] = [2,4]
graphWithCycle[2] = [3] #graphWithCycle[2] = [3,6]
graphWithCycle[3] = [5,11]#graphWithCycle[3] = [5,11]
graphWithCycle[4] = [2]#graphWithCycle[4] = [2]
graphWithCycle[5] = [4]
graphWithCycle[6] = [7]
graphWithCycle[7] = [8]
graphWithCycle[8] = [9]
graphWithCycle[9] = [10]
#graphWithCycle[10] = [2]
graphWithCycle[11] = [2]

bookKeepingDict = {}
node = 2
startFlag = True
cycleNode = 2
cycleNodeFlag = False
print("outsied function, cycleNodeFlag",cycleNodeFlag)
print(depthFirstTraversal(graphWithCycle,node,cycleNode,cycleNodeFlag,bookKeepingDict,startFlag ))
print("CycleLength:",smallestCycleTime)
