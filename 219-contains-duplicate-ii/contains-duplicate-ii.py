class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        c=set()
        
        for i in range(len(nums)):
            if nums[i] in c:
                return True
            c.add(nums[i])
            if len(c)>k:
                c.remove(nums[i-k])
        return False