# 33. Search in Rotated Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/search-in-rotated-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-26 23:54 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.4 MB (beats 77.8688%)


<!-- leetgit:submissionId=2121174094 codeHash=9212ba4718d8f4f83070f075be50aec56a564be4b1f347e318eab76c874fcb14 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # Run loop while valid search space exists
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # If target found at mid, return index
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # If target lies in left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # Target not found
        return -1
```
