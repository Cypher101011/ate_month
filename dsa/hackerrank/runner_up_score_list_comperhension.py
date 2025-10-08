if __name__ == "__main__":

    # arr =list(input().split())
    arr=[1,5,2.3,3,4]
    n=len(arr)
    print(arr)
def bubbleSort(arr,n):
    swapped =False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
            if not Swapped:
                break
        
            
    
        return arr
print(arr)
