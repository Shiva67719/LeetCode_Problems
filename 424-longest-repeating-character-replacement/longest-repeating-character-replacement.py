class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        r=0
        le=0
        c=0
        max_freq=0
        while r<len(s):
            d[s[r]]=d.get(s[r],0)+1
            max_freq=max(max_freq,d[s[r]])
            while (r-le+1)-max_freq>k:
                d[s[le]]-=1
                if d[s[le]]==0:
                    d.pop(s[le])
                le+=1
            c=max(c,r-le+1)
            r+=1
        return c