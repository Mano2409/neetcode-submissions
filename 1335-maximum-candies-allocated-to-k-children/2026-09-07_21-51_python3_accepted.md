# 1335. Maximum Candies Allocated to K Children
  
<br>**Problem:** https://leetcode.com/problems/maximum-candies-allocated-to-k-children/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-07 21:51 local time

**Runtime:** 348 ms (beats 78.87720000000016%)
**Memory:** 30.3 MB (beats 26.29239999999999%)


<!-- leetgit:submissionId=2134119490 codeHash=feaffccd780f3ddaa281e7ff2c06e1913547253cf3fc358afad02ad86cc10340 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low=1
        high=max(candies)
        ans=0
        while low<=high:
            mid=(low+high)//2
            final=self.func(candies,k,mid)
            if final>=k:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def func(self,candies,k,mid):
        total=0
        for i in candies:
            total+=(i//mid)
        return total

```
