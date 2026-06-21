class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) + 1  # Count VALUE
        
        return max(seen, key=seen.get)  # Return element with max count