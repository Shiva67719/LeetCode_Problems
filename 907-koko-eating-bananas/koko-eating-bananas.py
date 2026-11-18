class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # s=0
        # e=len(piles)-1
        def fun(m):
            count=0
            for i  in piles:
                count+=i//m
                if i%m!=0:
                    count+=1
            return count
        start=1
        end=max(piles)
        while start<end:
            mid=(start+end)//2
            k=fun(mid)
            if k<=h:
                end=mid
            else:
                start=mid+1
        return start

