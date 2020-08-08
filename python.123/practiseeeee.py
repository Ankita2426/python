def insertionsort(arr):
    for i in range(1,len(arr)):
        a = arr[i]
        j = i-1
        while j>=0 and a<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = a
arr = [23,4,0,1,5,7,8,4,56,7,4,465,778,4,56,33,5]
insertionsort(arr)
print(arr)
    
        
