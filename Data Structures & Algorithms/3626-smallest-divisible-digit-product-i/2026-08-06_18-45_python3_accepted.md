# 3626. Smallest Divisible Digit Product I
  
<br>**Problem:** https://leetcode.com/problems/smallest-divisible-digit-product-i/<br>

**Difficulty:** Easy<br>
**Topics:** Math, Enumeration<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-06 18:45 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.1 MB (beats 99.18700000000001%)


<!-- leetgit:submissionId=2096702995 codeHash=bad44f70b8daf1a02197d5e0ef19e6fa1439eb5fc8ba9963812714370ab67918 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        track = True

        while track:
            product = 1
            copy = n

            while copy != 0:
                digits = copy % 10
                copy = copy // 10
                product *= digits

            if product % t == 0:
                return n
            else:
                n += 1
```
