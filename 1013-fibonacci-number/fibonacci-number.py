class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        a=0
        b=1
        l=[]
        count=0
        while count<n:
            count+=1
            l.append(a)
            c=a+b
            a=b
            b=c
        return l[-1]+l[-2]
