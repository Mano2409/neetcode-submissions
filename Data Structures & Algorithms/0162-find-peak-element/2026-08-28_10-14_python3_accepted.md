# 162. Find Peak Element
  
<br>**Problem:** https://leetcode.com/problems/find-peak-element/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-28 10:14 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 96.52690000000001%)


<!-- leetgit:submissionId=2122536095 codeHash=d303ec9775249968cd5d20ce11929af626aaffe5e61fe1b5442f4589e2d7d84a notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        
        low=1
        high=n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                low=mid+1
            else:
                high=mid-1
        return -1

                
```
