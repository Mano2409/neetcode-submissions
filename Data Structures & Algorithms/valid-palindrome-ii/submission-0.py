class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                skip=s[left+1:right+1]
                skipr=s[left:right]
                return skip==skip[::-1]or skipr==skipr[::-1]
            left+=1
            right-=1
        return True