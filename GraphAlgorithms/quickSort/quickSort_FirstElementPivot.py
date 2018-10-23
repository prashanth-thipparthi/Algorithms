def partition(arr,low,high):

    pivot_value = arr[low]

    i = j = low + 1

    while j <= high:
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    #print(h - l)
    return i-1

def quickSort(arr,low,high):
    if(low<high):
        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)

arr1 = [4,5,7,2,3]
arr1 = [4,8,1,13,15,9]
quickSort(arr1,0,len(arr1)-1)
#(p,arr) = partition(arr1,0,len(arr1)-1)
#print(p)
print(arr1)
