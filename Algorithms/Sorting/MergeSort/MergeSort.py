import math

def merge(arr,low,mid,high):

    n1 = mid - low+1
    n2 = high-mid

    i = 0
    leftArr = [0] * n1
    rightArr = [0] * n2
    while i< n1:
        leftArr[i] = arr[low+i]
        i+=1
    j = 0
    while j < n2:
        rightArr[j] = arr[mid+1+j]
        j+=1

    i = j = 0
    l = low
    while i < n1 and j < n2:
        if(leftArr[i] <= rightArr[j]):
            arr[l] = leftArr[i]
            i+=1
        else:
            arr[l] = rightArr[j]
            j+=1
        l+=1
    while i < n1:
        arr[l] = leftArr[i]
        l+=1
        i+=1
    while j < n2:
        arr[l] = rightArr[j]
        l+=1
        j+=1
    return arr

def mergeSort(arr,low,high):
    if(low < high):
        mid = math.floor((low + high)/2)
        mergeSort(arr,low,mid)
        mergeSort(arr, mid +1, high)
        arr = merge(arr,low,mid,high)
        return arr

def mergeSort_aux(arr):
    length = len(arr)
    low = 0
    high = length - 1
    mergeSort(arr,low,high)
    return arr

arr = [7,3,6,1,9,10,12,4,2,8,5]
print(mergeSort_aux(arr))