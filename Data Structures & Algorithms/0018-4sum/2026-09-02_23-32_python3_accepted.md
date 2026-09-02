# 18. 4Sum
  
<br>**Problem:** https://leetcode.com/problems/4sum/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-02 23:32 local time

**Runtime:** 395 ms (beats 65.48140000000022%)
**Memory:** 19.4 MB (beats 54.21560000000001%)


<!-- leetgit:submissionId=2128814036 codeHash=01aef4398b709e3e1038896dbf58e435e6cd0a03cd679cc15835baaceac5d194 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                # Skip duplicate j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1

                    elif total > target:
                        right -= 1

                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # Skip duplicate left
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate right
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return ans
```
