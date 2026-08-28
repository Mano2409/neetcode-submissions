# 374. Guess Number Higher or Lower
  
<br>**Problem:** https://leetcode.com/problems/guess-number-higher-or-lower/<br>

**Difficulty:** Easy<br>
**Topics:** Binary Search, Interactive<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-28 13:40 local time

**Runtime:** 56 ms (beats 5.166999999999992%)
**Memory:** 19.2 MB (beats 29.795899999999996%)


<!-- leetgit:submissionId=2122685821 codeHash=18c5791e76034f847dcedf806522baecfa2a20cbb26ad8bed20afc246ee8e578 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=0
        right=n
        while left<=right:
            mid=left+((right-left)//2)
            result =guess(mid)
            if result ==0:
                return mid
            elif result ==1:
                left=mid+1
            else:
                right=mid-1
        return -1
```
