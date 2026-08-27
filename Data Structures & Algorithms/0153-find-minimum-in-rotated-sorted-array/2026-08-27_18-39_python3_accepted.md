# 153. Find Minimum in Rotated Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-27 18:39 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.4 MB (beats 25.83339999999999%)


<!-- leetgit:submissionId=2121914771 codeHash=a59c71ee7eb2e02fea0326d781b297da4bc3f6ad63da9643445e3de4d695cbd9 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]<nums[high]:
                high=mid
            else:
                low=mid+1
        return nums[low]
```
