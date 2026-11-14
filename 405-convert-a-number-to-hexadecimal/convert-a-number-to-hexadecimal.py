class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return '0'
        
        if num<0:
            num+=2**32

        digit = "0123456789abcdef"
        ans = ""

        while num:
            r=num%16
            ans=digit[r]+ans
            num//=16

        return ans