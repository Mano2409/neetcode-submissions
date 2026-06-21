from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=Counter(nums)
        res=[x[0] for x in s.most_common(k)]
        return res