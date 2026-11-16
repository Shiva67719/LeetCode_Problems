class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # else:
        #     return -1

        s=0
        e=len(nums)-1
        #lb=hb=len(nums)
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                return mid
            #aditya loves ashritha
            elif nums[mid]> target:
                e=mid-1
            else:
                s=mid+1
        return -1