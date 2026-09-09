class Solution:
    def thirdMax(self, nums: List[int]) -> int: 
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)<3:
            return nums[0]
        count=0
        for i in nums:
            count+=1
            if count==3:
                return i
    
            
