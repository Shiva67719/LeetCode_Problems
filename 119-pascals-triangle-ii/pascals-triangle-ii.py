class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        l=[]
        for i in range(1,rowIndex+1+1):
            k=1
            ll=[]
            for j in range(1,i+1):
                ll.append(k)
                k=k*(i-j)//j
            l.append(ll)
        return l[-1]
        