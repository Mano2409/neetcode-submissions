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