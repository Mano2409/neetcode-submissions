# 2572. Append Characters to String to Make Subsequence
  
<br>**Problem:** https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/<br>

**Difficulty:** Medium<br>
**Topics:** Two Pointers, String, Greedy<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-15 02:29 local time

**Runtime:** 31 ms (beats 36.0423%)
**Memory:** 21.4 MB (beats 7.420499999999993%)


<!-- leetgit:submissionId=2142001348 codeHash=0ffb332a95d84a752276dc7d69f00d53c67fbd9e285856ddf8f7a987b5f244fe notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sample1 = list(s)
        sample2 = list(t)

        left1 = 0
        left2 = 0

        for _ in range(len(s)):
            if left2 < len(t) and sample1[left1] == sample2[left2]:
                left1 += 1
                left2 += 1
            else:
                left1 += 1

        return len(sample2) - left2
```
