from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=Counter(nums)
        res=[x for x,y in s.most_common(k)]
        return res