def bubbleSort(arr):
    length = len(arr)
    i = 0
    j = 1
    '''''
    For every iteration of i, comapare the two adjacent elements in the array using  index 'j'
    and swap the elements if a[j] > a[j+1], In this manner for every iteration of 'i', you'll be
    bubbling down largest element to the end of the array. 
    '''''
    while i < length-1:
        j= 0
        while j < length-i-1:
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
            j+=1
        i+=1

    return arr

arr = [3,5,7,9,1,2,11,13,15]

print(bubbleSort(arr))