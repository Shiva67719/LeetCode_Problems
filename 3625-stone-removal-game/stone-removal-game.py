class Solution:
    def canAliceWin(self, n: int) -> bool:
        t=0
        for i in range(10,0,-1):
            if n<i:
                break

            n-=i
            t+=1
        return t%2==1