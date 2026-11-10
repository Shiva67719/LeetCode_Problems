class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p=1
        d=1
        for i in range(time):
            p=p+d
            if p==n or p==1:
                d=-d
        return p