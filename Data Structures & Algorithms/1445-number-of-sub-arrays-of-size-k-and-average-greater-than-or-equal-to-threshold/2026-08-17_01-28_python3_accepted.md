# 1445. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
  
<br>**Problem:** https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Sliding Window<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-17 01:28 local time

**Runtime:** 42 ms (beats 71.1579%)
**Memory:** 29.8 MB (beats 80.6264%)


<!-- leetgit:submissionId=2109441778 codeHash=d81b827f7574b8849980f2b947edaf756e676eab3987662182b6ce758ae85c0c notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = sum(arr[:k])

        for i in range(k, len(arr) + 1):

            # Check current window
            if window_sum >= k * threshold:
                count += 1

            # Move the window
            if i < len(arr):
                window_sum = window_sum - arr[i-k] + arr[i]

        return count
```
