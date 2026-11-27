class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:

	# if firstList == [] or secondList == []:
	# 	return []

        # res = []
        # a=0
        # b=0

        # while a < len(firstList) and b < len(secondList):
        #     l = max(firstList[a][0], secondList[b][0])
        #     r = min(firstList[a][1], secondList[b][1])

        #     if l <= r :
        #         res.append([l, r])

        #     if firstList[a][1] < secondList[b][1]:
        #         a += 1

        #     else:
        #         b += 1        

        # return res


        A=firstList
        B=secondList
        res=[]
        s=0
        e=0
        while s<len(A) and e<len(B):
            l=max(A[s][0],B[e][0])
            r=min(A[s][1],B[e][1])
            if l<=r:
                res.append([l,r])
            if A[s][1]<B[e][1]:
                s+=1
            else:
                e+=1
        return res