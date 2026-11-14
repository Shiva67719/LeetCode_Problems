class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for i in d:
            if d[i]==1:
                return i