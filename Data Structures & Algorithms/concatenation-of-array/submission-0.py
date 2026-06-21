class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        s = nums  # or nums.copy() to be safe
        for i in range(len(nums)):
            s.append(nums[i])  # Append VALUE, not index
        return s  # Outside loop!