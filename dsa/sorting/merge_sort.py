def merge(arr,l,r):
    a=[]
    b=[]
    a=arr[l:mid+1]
    b=arr[mid+1:r]

    i,j,k=0,0,l
    while k<=r:
        if j==len(b):
            arr[k]=a[i]
            i+=1
            k+=1
        elif i==len(a):
            arr[k]=b[j]
            j+=1
            k+=1
        elif a[i]<b[j]:
            arr[k]=a[i]
            i+=1
            k+=1
        else:
            arr[k]=b[j]
            j+=1
            k+=1



def mergeSort(arr,l,r):
    if l>=r:
        return
    mid=(l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)

    merge(arr,l,mid,r)

def sortArray():
   print(mergeSort([1,2,31,4,2,1,5,2,5,2]))

sortArray()