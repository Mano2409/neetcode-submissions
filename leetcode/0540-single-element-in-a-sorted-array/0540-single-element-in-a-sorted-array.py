from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge cases for small arrays / ends
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        # Search space boundaries (skipping already checked 0 and n-1)
        low = 1
        high = n - 2
        
        while low <= high:
            mid = (low + high) // 2
            
            # Found the unique element
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            # Check if we are in the left half (valid pairs pattern)
            # Even index matching right OR Odd index matching left
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1  # Move right
            else:
                high = mid - 1  # Move left
                
        return -1