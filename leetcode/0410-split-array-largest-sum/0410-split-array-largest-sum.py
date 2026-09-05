class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            final=self.func(nums,mid)

            if final>k:
                low=mid+1
    
            else:
                high=mid-1
        return low

    def func(self,nums,mid):
        sum=0
        counter=1
        for i in nums:
            if sum+i<=mid:
                sum+=i
            else:
                counter+=1
                sum=0
                sum+=i
        return counter


        