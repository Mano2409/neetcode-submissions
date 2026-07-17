class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return True
        new="".join(filter(str.isalnum, s))
        k=new.lower()
        low=0
        high=len(new)-1
        while low<high:
            if k[low]!=k[high]:
                return False

            low+=1
            high-=1
        return True 