from array import *

# Create integer array
arr = array('i', [2, 2, 5, 5, 8, 8])

# Create double (float) array
arr2= array('d', [1, 3, 526, 6, 34])

def traverse_array(arr):
    for i in arr:
        print(i)

traverse_array(arr)
print("-----")
traverse_array(arr2)

def find_element(arr,value):
    for i in range(len(arr)):
        if arr[i]==value:
            return i+1
        
find_element(arr, 3)

def accessElement(ar,index):
    if index>len(ar):
        print("there is not any elemnet in the index")
    else:
        print(ar[index])
    
print(accessElement(arr,1))

def searchInaArray(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "the element deoes not exist in this array"
    
print(searchInaArray(arr, 5))


# delete array elemetn
print(arr)
arr.remove(2)
print(arr)