class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        for i in range(len(arr) - k + 1):
            subarray = arr[i:i+k]
            total = sum(subarray)

            if total >= k * threshold:
                count += 1

        return count