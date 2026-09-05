# 2000. Minimum Speed to Arrive on Time
  
<br>**Problem:** https://leetcode.com/problems/minimum-speed-to-arrive-on-time/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-05 23:01 local time

**Runtime:** 1054 ms (beats 91.94139999999982%)
**Memory:** 33.4 MB (beats 81.56289999999997%)


<!-- leetgit:submissionId=2131992771 codeHash=e149e3f447c440bc8c6bd60bb4fecacdb9b64214e9942536bf0c656785b15116 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
import math
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        low = 1
        high = 10**7
        ans = 10**7

        while low <= high:
            mid = (low + high) // 2
            final = self.func(dist, mid)

            if final <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def func(self, dist, mid):
        total = 0
        for i in dist[:-1]:
            total += math.ceil(i / mid)
        total += dist[-1] / mid
        return total
```
