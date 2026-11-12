class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=0
        while x>0 or y>0:
            a=x%2
            b=y%2
            if a!=b:
                c+=1
            x=x//2
            y=y//2
        return c