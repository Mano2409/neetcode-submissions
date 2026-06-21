from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=Counter(nums)
        return max(k,key=k.get)