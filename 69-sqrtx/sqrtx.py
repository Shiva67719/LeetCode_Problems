class Solution:
    def mySqrt(self, x: int) -> int:
        # if x==0:
        #     return 0
        # for i in range(1,x+1):
        #     # a=i*i
        #     # if a==x:
        #     #     return a
        #     # elif a>x:
        #     #   return a-1
        #     if i * i==x:
        #         return i
        #     elif i*i>x:
        #         return i-1
        if x==0:
            return 0
        s=1
        e=x
        while s<=e:
            mid=(s+e)//2
            if mid*mid==x:
                return mid
            elif mid * mid<x:
                s=mid+1
            else:
                e=mid-1
        return e