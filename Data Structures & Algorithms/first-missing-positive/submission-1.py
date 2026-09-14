class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            index=nums[i]-1
            if index==i:
                i+=1
            
                
            elif 0 <= index < len(nums) :
                if nums[i]==nums[index]:
                    i+=1
                else:

                    nums[index],nums[i]=nums[i],nums[index]
                    
                
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]==i+1:
                continue
            else:
                return i+1
        return len(nums)+1