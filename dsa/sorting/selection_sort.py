def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        minimum=arr[i]
        index=i
        for j in range(i+1,n):
            if minimum>arr[j]:
                minimum=arr[j]
                index=j
        arr[i],arr[index]=arr[index],arr[i]
    return arr

print(selection_sort([1,2,31,4,2,1,5,2,5,2]))