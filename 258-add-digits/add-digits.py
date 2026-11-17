class Solution:
    def addDigits(self, num: int) -> int:
        # if num==0:
        #     return 0

        while num>=10:
            d=0
            while num>0:
                r=num%10
                d=d+r
                num=num//10
            num=d
        return num

            #return num%9 if num%9!=0 or num==0 else 9