# 1056. Capacity To Ship Packages Within D Days
  
<br>**Problem:** https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-30 13:21 local time

**Runtime:** 211 ms (beats 76.62270000000021%)
**Memory:** 23.9 MB (beats 67.45590000000001%)


<!-- leetgit:submissionId=2124791322 codeHash=608c6110890a100a8646294a0feecd77973d74da6dc9afaad92d2558fcc85e46 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=sum(weights)
        while low<=high:
            mid=(low+high)//2
            final=self.func(weights,mid) 
            if final<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
           
    def func(self,weights,mid):
        total=1
        streak=0
        for i in weights:
            if streak+i<=mid:
                streak+=i
            else:
                total+=1
                streak=i
        return total




        

```
