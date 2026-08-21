# 35. Search Insert Position
  
<br>**Problem:** https://leetcode.com/problems/search-insert-position/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-21 23:21 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20 MB (beats 11.617599999999982%)


<!-- leetgit:submissionId=2115367294 codeHash=1c62f99d216fafde643a8c351c2cfab6c1f33db38a6faf45b6734d25984a5f65 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans
```
