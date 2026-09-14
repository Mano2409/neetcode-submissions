# 41. First Missing Positive
  
<br>**Problem:** https://leetcode.com/problems/first-missing-positive/<br>

**Difficulty:** Hard<br>
**Topics:** Array, Hash Table<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-15 03:31 local time

**Runtime:** 55 ms (beats 37.477000000000054%)
**Memory:** 31.1 MB (beats 37.68879999999998%)


<!-- leetgit:submissionId=2142024441 codeHash=8b3b1aeadadf965662c5560c2702c3e7dacc39c32efdec00b128a8bcaff3c447 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left=0
        while left<len(nums):
            index=nums[left]-1
            if index==left:
                left+=1
            elif 0<=index<len(nums):
                if nums[left]==nums[index]:
                    left+=1
                else:
                    nums[index],nums[left]=nums[left],nums[index]
            else:
                left+=1
        for i in range(len(nums)):

            if  nums[i]==i+1:
                continue
            else:
                return i+1
        return len(nums)+1
        
```
