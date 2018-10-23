def insertionSort(arr):
    '''
    Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
    We pick a element in the array, at index i , and assignj = i-1. Now,we compare a[i] and a[j],
    if a[j] is grater we shift a[j] toone position right and decrement j.Like wise wherever the condition
    fails you drop a[i] overthere.
    '''
    length = len(arr)
    i = 1
    #j = 1
    while i < length:
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        i+=1
    return arr

arr = [8,10,17,15,3,1,9,2,5,6,11]
print (insertionSort(arr))