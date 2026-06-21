class Solution:
    def isPalindrome(self, s: str) -> bool:
      
        new="".join(filter(str.isalnum, s))
        new=new.lower()
        low=0
        high=len(new)-1
        while low<high:
            if new[low]!=new[high]:
                return False
            low+=1
            high-=1
        return True 
        