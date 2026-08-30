# 1408. Find the Smallest Divisor Given a Threshold
  
<br>**Problem:** https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-30 12:08 local time

**Runtime:** 129 ms (beats 61.684399999999975%)
**Memory:** 24.6 MB (beats 14.1481%)


<!-- leetgit:submissionId=2124727314 codeHash=a64562549101baa70f93698e07c117c5119320fa4e14d5e788413dabe21a302b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=max(nums)
        while low<=high:
            mid=(low+high)//2
            final=self.func(nums,mid)
            if final<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans




   
    def func(self,nums,mid):
        total=0
        for i in nums:
            total+=math.ceil(i/mid)
        return total
```
