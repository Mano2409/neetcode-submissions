class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            time=self.func(piles,mid)
            if time<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def func(self,piles,mid):
        total=0
        for i in piles:
            total+=math.ceil(i/mid)
        return total

