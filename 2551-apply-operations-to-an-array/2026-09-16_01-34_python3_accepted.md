# 2551. Apply Operations to an Array
  
<br>**Problem:** https://leetcode.com/problems/apply-operations-to-an-array/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-16 01:34 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.4 MB (beats 62.88559999999998%)


<!-- leetgit:submissionId=2143039712 codeHash=3d301682808af50ef2d5e6d453d77cc8d31f822ac644095592f54144cd54e8d7 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        
            i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        return  nums
```
