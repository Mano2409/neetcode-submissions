class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low=1
        high=max(position)-min(position)
        while low<=high:
            mid=(low+high)//2
            final=self.func(position,mid,m)
            if final==True:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def func(self,position,mid,m):
        tracker=1
        last=position[0]
        for  i in range(1,len(position)):
            if position[i]-last>=mid:
                tracker+=1
                last=position[i]
        return tracker>=m




        