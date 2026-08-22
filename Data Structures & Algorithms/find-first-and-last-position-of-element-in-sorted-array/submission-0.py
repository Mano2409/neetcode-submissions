class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr=[-1,-1]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)
            if nums[mid]==target:
                arr[0]=mid
                right=mid-1
            elif nums[mid]>target:
                right=mid -1
            else:
                left=mid+1
        low=0
        high=len(nums)-1
        while low <=high:
            mid=(low+high)//2
            if nums[mid]==target:
                arr[1]=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return arr



