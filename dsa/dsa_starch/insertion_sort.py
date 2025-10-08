array = [5, 3, 4, 1, 2]

# for i =1 to n-1:
#     key=[i]
#     j=i-1

#     while j>=0 and A[j]> key:
#         a[j+1]=a[j]
#         j=j-1

#     a[j+1]=key

def insertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1

        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array

print(insertionSort(array))

