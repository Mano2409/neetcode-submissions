# 1421. Find Numbers with Even Number of Digits
  
<br>**Problem:** https://leetcode.com/problems/find-numbers-with-even-number-of-digits/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Math<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-09 19:21 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.4 MB (beats 6.536199999999987%)


<!-- leetgit:submissionId=2136396018 codeHash=979214b891ddc0370e923e15058cb3965bbfea79162048a84bdc2f8006038138 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count
        
```
