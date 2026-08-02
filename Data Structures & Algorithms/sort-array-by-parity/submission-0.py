class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        left=0
        right=len(nums)
        pos=0
        while left<right:
            if nums[left]%2==0:
                nums[left],nums[pos]=nums[pos],nums[left]
                left+=1
                pos+=1
            else:
                left+=1
        return nums


     
        