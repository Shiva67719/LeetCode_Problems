class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        #nums.sort()
        s=0
        e=len(nums)-1
        while s<e:
            mid=(s+e)//2
            if nums[mid]<nums[mid+1]:
                s=mid+1
            else:
                e=mid
        return s