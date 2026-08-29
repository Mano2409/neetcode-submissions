# 1605. Minimum Number of Days to Make m Bouquets
  
<br>**Problem:** https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-30 00:13 local time

**Runtime:** 290 ms (beats 83.46150000000002%)
**Memory:** 32.3 MB (beats 23.55210000000002%)


<!-- leetgit:submissionId=2124260864 codeHash=70913076386797f801876d853b9e848f4236c7280b5f029d81b819c092bc71ca notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=high
        while low<=high:
            mid=(low+high)//2
            final=self.check(bloomDay,mid,k)
            if final >=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
            
        return ans
            
    def check(self,bloomDay,mid,k):
        total=0
        streak=0
        
        for i in bloomDay:
            

            if i<=mid:
                streak+=1
                if streak==k:
                    streak=0
                    total+=1
            else:
                streak=0
        return total
   
        
```
