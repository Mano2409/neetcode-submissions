# 81. Search in Rotated Sorted Array II
  
<br>**Problem:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-27 17:09 local time

**Runtime:** 3 ms (beats 7.577500000000003%)
**Memory:** 19.6 MB (beats 31.955400000000004%)


<!-- leetgit:submissionId=2121844766 codeHash=eb0a7fcb4009b5a2998a3af21670ac4902c73f3698fe7f11cd47b2537e40dc82 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0 
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True 
            elif nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target <=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False 
```
