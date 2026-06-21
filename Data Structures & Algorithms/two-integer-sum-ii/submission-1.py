class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]  # ✅ FIX: numbers[right], not reight
            if sum == target:
                return [left + 1, right + 1]  # ✅ FIX: right+1, not reight
            if sum > target:
                right -= 1
            else:
                left += 1
        return []