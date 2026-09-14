class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left=0
        while left<len(nums):
            index=nums[left]-1
            if index==left:
                left+=1
            elif 0<=index<len(nums):
                if nums[left]==nums[index]:
                    left+=1
                else:
                    nums[index],nums[left]=nums[left],nums[index]
            else:
                left+=1
        for i in range(len(nums)):

            if  nums[i]==i+1:
                continue
            else:
                return i+1
        return len(nums)+1
        