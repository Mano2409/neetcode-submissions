class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low=1
        high=max(candies)
        ans=0
        while low<=high:
            mid=(low+high)//2
            final=self.func(candies,k,mid)
            if final>=k:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def func(self,candies,k,mid):
        total=0
        for i in candies:
            total+=(i//mid)
        return total
