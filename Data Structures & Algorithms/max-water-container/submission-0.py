class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        re = 0  # ✅ Initialize BEFORE loop
        
        while left < right:
            s = right - left
            s2 = min(heights[left], heights[right])
            mx = s * s2
            re = max(re, mx)  # ✅ Compare with previous max
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return re  # ✅ Return AFTER loop ends