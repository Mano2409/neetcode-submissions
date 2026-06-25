class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=[]
        for i in nums1:
            num3.append(i)
        for j in nums2:
            num3.append(j)
        n=len(num3)
        num3.sort()
        if n%2==1:
            return num3[n//2]
        else:
            d=((num3[(n//2)-1])+num3[n//2])/2.0
            return d
        