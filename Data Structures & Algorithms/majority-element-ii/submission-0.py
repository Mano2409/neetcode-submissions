class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n = n // 3

        ss = {}
        for i in nums:
            ss[i] = ss.get(i, 0) + 1

        s = [x for x, y in ss.items() if y > n]
        return s