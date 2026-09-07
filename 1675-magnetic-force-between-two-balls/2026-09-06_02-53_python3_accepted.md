# 1675. Magnetic Force Between Two Balls
  
<br>**Problem:** https://leetcode.com/problems/magnetic-force-between-two-balls/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-06 02:53 local time

**Runtime:** 503 ms (beats 59.26679999999982%)
**Memory:** 31.5 MB (beats 48.206599999999995%)


<!-- leetgit:submissionId=2132168433 codeHash=d9e0139bc8b11026cfe034b9c12760eafe87c6d5d95168ca756548a8d08503db notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low=1
        high=max(position)-min(position)
        while low<=high:
            mid=(low+high)//2
            final=self.func(position,mid,m)
            if final==True:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def func(self,position,mid,m):
        tracker=1
        last=position[0]
        for  i in range(1,len(position)):
            if position[i]-last>=mid:
                tracker+=1
                last=position[i]
        return tracker>=m




        
```
