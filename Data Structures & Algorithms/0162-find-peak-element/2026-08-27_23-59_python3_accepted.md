# 162. Find Peak Element
  
<br>**Problem:** https://leetcode.com/problems/find-peak-element/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-27 23:59 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.4 MB (beats 39.786000000000016%)


<!-- leetgit:submissionId=2122262521 codeHash=0d67bf0abf7f515fa431c8531d5b353fff1f971884437aea26f35fdffc91cf63 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low< high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:
                high=mid
            else:
                low=mid+1
        return low
        
```
