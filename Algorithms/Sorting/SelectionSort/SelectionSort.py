def selectionSort(arr):
    '''''
    selection sort, selects the smallest element in the array and places it at the starting of the array.
    index 'j' will search for smallest element and places it at the index 'i' and 'i' slides through
    '''''
    length = len(arr)
    i = 0
    j = i+1
    min_index = i
    #One by one move boundary of unsorted subarray
    while i< length:
        #Find the minimum element in unsorted array
        min_index = i
        j = i+1
        while j < length:
            if(arr[j]<arr[min_index]):
                min_index = j
            j+=1
        #Swap the found minimum element with the first element
        arr[i],arr[min_index] = arr[min_index],arr[i]
        i+=1
    return arr

arr = [9,2,5,7,1,5,10,12,16]
print(selectionSort(arr))