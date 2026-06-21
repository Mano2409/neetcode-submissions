class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        # Create hash array
        hash_arr = [0] * (n + 1)
        
        # Mark which numbers exist
        for num in nums:
            hash_arr[num] += 1
        
        # Find missing number (0 to n)
        for i in range(n + 1):
            if hash_arr[i] == 0:
                return i
        
        return -1