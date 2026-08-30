class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=sum(weights)
        while low<=high:
            mid=(low+high)//2
            final=self.func(weights,mid)
            if final<=days:
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans

    def func(self,weights,mid):
        total=1
        streak=0
        for i in weights:
            if streak+i<=mid:
                streak+=i

            else:
                total+=1
                streak=0
                streak+=i
        return total

