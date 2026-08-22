# 34. Find First and Last Position of Element in Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-22 15:05 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.7 MB (beats 7.954699999999995%)


<!-- leetgit:submissionId=2115963917 codeHash=ee333340e007cd3737b6d618552825ccece89b7d88d023caae0aacc09cd41545 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = [-1, -1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                arr[0] = mid
                right = mid - 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                arr[1] = mid
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return arr
```
