class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        coun = 0
        el = 0
        n = len(nums)

        for i in range(n):
            if coun == 0:
                coun = 1
                el = nums[i]
            elif el == nums[i]:
                coun += 1
            else:
                coun -= 1

        coun = 0   # important bro

        for i in range(n):
            if el == nums[i]:
                coun += 1

        if coun > n // 2:
            return el

        return -1