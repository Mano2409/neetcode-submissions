class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        s = {}
        for x in nums:
            s[x] = s.get(x, 0) + 1
        ss=sorted(s.items(),key=lambda x:(x[1],-x[0]))
        res=[y for y,x in ss for i in range(x)]
        return res