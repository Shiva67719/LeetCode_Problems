class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        p=paragraph.lower()
        for ch in "!?',;.":
            p=p.replace(ch," ")
        w=p.split()
        ws=set(banned)
        d={}
        for i in w:
            if i in ws:
                continue
            d[i]=d.get(i,0)+1
        return max(d,key=d.get)