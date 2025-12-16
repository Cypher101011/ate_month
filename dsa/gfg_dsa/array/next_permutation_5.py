class Solution:
    def nextPermutation(self,arr):
        n = len(arr)

    i=n
    while arr[i-2]<[i-1] and arr[i-2]:
        i-=1
    if i<2:
        arr.reverse()
        return
    j=n-1
    while arr[j]<=arr[i-2]:
        j-=1

    arr[i-2],arr[j]=arr[j],arr[i]


left,right =i-1,n-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1