class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i,i+1
        # else:
        #     return -1,-1

        # s=0
        # e=len(nums)-1
        # while s>=e:
        #     mid=(s+e)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]>=target:
        #         e=mid-1
        #     else:
        #         s=mid+1
        # return -1,-1

        s=0
        e=len(nums)-1
        first=len(nums)
        #lb=hb=len(nums)
        while s<=e:
            mid=(s+e)//2
            if nums[mid]>=target:
                first=mid
                e=mid-1
            else:
                s=mid+1
        if first==len(nums) or nums[first]!=target:
            return[-1,-1]
        last=len(nums)
        s=0
        e=len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]>target:
                last=mid
                e=mid-1
            else:
                s=mid+1
        return[first,last-1]