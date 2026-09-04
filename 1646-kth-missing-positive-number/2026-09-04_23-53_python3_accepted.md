# 1646. Kth Missing Positive Number
  
<br>**Problem:** https://leetcode.com/problems/kth-missing-positive-number/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-04 23:53 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 76.42369999999998%)


<!-- leetgit:submissionId=2131036664 codeHash=84774d7f834b29eb7d96c58d2fefa4bcd0abf81d182827f18beaa9697d1826b3 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                low=mid+1
            else:
                high=mid-1
        return high+k+1
        
```
