class Solution:
    def findMin(self, nums: list[int]) -> int:
        s=0
        e=len(nums)-1
        while s<e:
            mid=(s+e)//2
            if nums[mid]<nums[e]:
                e=mid
            elif nums[mid]>nums[e]:
                s=mid+1
            else:
                e-=1
        return nums[s]