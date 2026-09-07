# 2737. Row With Maximum Ones
  
<br>**Problem:** https://leetcode.com/problems/row-with-maximum-ones/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Matrix<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-08 00:14 local time

**Runtime:** 4 ms (beats 83.3466%)
**Memory:** 19.9 MB (beats 74.26299999999999%)


<!-- leetgit:submissionId=2134311810 codeHash=d2e57ddcbdf30e108b52d2ea37ef48945e8cc1655629334af418e6facd53d73f notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index=0
        count=0
        for i in range(len(mat)):
            c=mat[i].count(1)
            if c>count:
                count=c
                index=i
        return [index,count]
```
