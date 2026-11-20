class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        s=0
        e=0
        for i in range(len(nums)):
            if s==0 and e!=nums[i]:
                e=nums[i]
                s+=1
            elif e==nums[i]:
                s+=1
            else:
                s-=1
        return e