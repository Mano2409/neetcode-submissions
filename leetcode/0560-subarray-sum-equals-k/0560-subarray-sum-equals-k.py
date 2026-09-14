class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        has = {}
        su = 0
        count = 0
        
        for i in range(len(nums)):
            su += nums[i]
            
            if su == k:
                count += 1
            
            rem = su - k
            if rem in has:
                count += has[rem]
            
            if su not in has:
                has[su] = 0
            has[su] += 1
        
        return count
