def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n):
        isSwap=False
        for j in range(0,n-1-i):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                isSwap=True
        if not isSwap:
            return arr
    return arr
print(bubble_sort([1,2,3,4123,532,6,2,1,2]))

