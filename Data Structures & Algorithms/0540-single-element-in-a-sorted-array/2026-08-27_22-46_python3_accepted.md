# 540. Single Element in a Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/single-element-in-a-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-27 22:46 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 27.1 MB (beats 30.836600000000008%)


<!-- leetgit:submissionId=2122170978 codeHash=97f31d7fe6d24479ff85f8dd2d6f4726cfc6ffa8292aa4ba7ad76c2f6558d03f notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
   
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low = 1
        high = n - 2
        
        while low <= high:
            mid = (low + high) // 2
            
           
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
          
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1 
            else:
                high = mid - 1  
                
        return -1
```
