class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1 
        if n>0:
            return False
        else:
            return True  
sol=Solution()


print(sol.canPlaceFlowers([1,0,1,0,1], 1))