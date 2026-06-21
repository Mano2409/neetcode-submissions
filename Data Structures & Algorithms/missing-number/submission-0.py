class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n + 1):
            found = False

            for j in range(n):
                if nums[j] == i:
                    found = True
                    break

            if not found:
                return i