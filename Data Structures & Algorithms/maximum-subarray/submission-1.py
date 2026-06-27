class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxee = nums[0]

        for i in range(len(nums)):
            su = 0
            for j in range(i, len(nums)):
                su += nums[j]
                maxee = max(maxee, su)

        return maxee