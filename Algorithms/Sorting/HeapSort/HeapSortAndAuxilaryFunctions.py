import math

def extractMax(arr):
    length = len(arr)
    if length < 1:
        return "Heap Underflow"
    max = arr[0]
    arr[0] = arr[length-1]
    length = length - 1
    max_heapify(arr,length,0)
    del arr[length]
    return max

def increaseKeyValueInHeap(arr,index,newValue):
    if(newValue < arr[index]):
        return "key Error"
    arr[index] = newValue

    while index >=0 and arr[math.floor(index/2)]<arr[index]:
        arr[math.floor(index/2)],arr[index] = arr[index],arr[math.floor(index/2)]
        index = math.floor(index/2)

def insertKey(arr,keyValue):
    length = len(arr)-1
    arr.append(keyValue)
    print("inside insert:",arr)
    index = length+1
    while index>=0 and arr[math.floor(index/2)]<arr[index]:
        arr[math.floor(index / 2)], arr[index] = arr[index], arr[math.floor(index / 2)]
        index = math.floor(index / 2)

def max_heapify(arr,length,i):
    # length = len(arr)-1
    left = 2 * i
    right = 2 * i + 1
    if(left<= length and arr[left] > arr[i] ):
        largest = left
    else:
        largest = i
    if(right <= length and arr[right] > arr[largest]):
        largest = right
    if(largest != i):
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,length, largest)

def buildHeap(arr):
    length = len(arr)-1
    max_non_leaf_node_index = math.ceil(length/2) + 1
    i = max_non_leaf_node_index
    while i >= 0:
        max_heapify(arr,length,i)
        i-=1

def heapSort(arr):
    buildHeap(arr)
    print ("inside sort:",arr)
    length = len(arr)-1
    i = length
    while i> 0:
        arr[0],arr[i] = arr[i],arr[0]
        i-=1
        length = length - 1
        max_heapify(arr,length, 0)

arr = [1,5,6,8,14,16]
buildHeap(arr)
print(arr)
print ("max element:",extractMax(arr))
print(arr)
increaseKeyValueInHeap(arr,2,50)
print(arr)
# buildHeap(arr)
# print(arr)
insertKey(arr,900)
print(arr)
# buildHeap(arr)
# print(arr)
heapSort(arr)
print (arr)
#
