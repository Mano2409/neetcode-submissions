class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: empty array
        if not nums:
            return 0
        
        # Convert list to set for O(1) lookups
        num_set = set(nums)
        max_length = 0
        
        # Iterate through each unique number
        for num in num_set:
            # Only start counting if this is a SEQUENCE START
            # (i.e., the number before it doesn't exist)
            if num - 1 not in num_set:
                current_num = num        # Starting number
                current_length = 1       # At least 1 number in sequence
                
                # Count how long the consecutive sequence is
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update max length found so far
                max_length = max(max_length, current_length)
        
        return max_length