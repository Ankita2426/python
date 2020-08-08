def insertionsort(arr):
    for i in range(1,len(arr)):
        a = arr[i]
        j = i-1
        while j>=0 and a <arr[j]:
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1]= a
arr = [23,4,54,67,3,5,6]
insertionsort(arr)
print(arr)
