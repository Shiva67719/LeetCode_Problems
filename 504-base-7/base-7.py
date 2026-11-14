class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        c=1 if num < 0 else 0
        num=abs(num)
        res=""
        while num>0:
            res=str(num%7)+res
            num=num//7
        if c==1:
            return "-"+res
        return res