array=[1,2,3,3,5,2,53,234,6453,623,2452,245,223,2,3,1,3,-2,2]

A_sorted=sorted(array)

def BinarySearch(A_sorted,value):
    indeHigh=len(A_sorted)-1    
    indexLow=0

    while indexLow<=indeHigh:
        indexMid=round((indeHigh+indexLow)/2)

        if A_sorted[indexMid]==value:
            return indexMid
        if A_sorted[indexMid]<value:
            indexLow=indexMid+1
        else:
            indeHigh=indexMid-1
    return -1

print(BinarySearch(A_sorted,2))