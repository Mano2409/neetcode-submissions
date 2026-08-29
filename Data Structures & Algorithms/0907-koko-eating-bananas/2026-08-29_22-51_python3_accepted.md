# 907. Koko Eating Bananas
  
<br>**Problem:** https://leetcode.com/problems/koko-eating-bananas/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-29 22:51 local time

**Runtime:** 165 ms (beats 69.26019999999971%)
**Memory:** 20.5 MB (beats 81.48239999999997%)


<!-- leetgit:submissionId=2124172730 codeHash=1a0133c0b09a080c36f82c4278b556e603529ebb8eace795d04b64598a8a9d79 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            total=self.func(piles,mid)
            if total<=h:
                ans=mid
                high=mid-1

            else:
                low=mid+1
        return ans
    def func(self,piles,mid):
        final=0
        for i in piles:
            final+=math.ceil(i/mid)
        return final

        
```
