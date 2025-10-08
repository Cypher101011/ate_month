
array = [5, 3, 4, 1, 2]

def insertionSort(array):
    for i in range(len(array)):
        if array[i]>array[i+1]:
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
    
    return array
print(insertionSort(array))