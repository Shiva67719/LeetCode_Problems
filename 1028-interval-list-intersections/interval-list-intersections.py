class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:

	# if firstList == [] or secondList == []:
	# 	return []

        res = []
        a, b = 0, 0

        while a < len(firstList) and b < len(secondList):
            l = max(firstList[a][0], secondList[b][0])
            r = min(firstList[a][1], secondList[b][1])

            if l <= r :
                res.append([l, r])

            if firstList[a][1] < secondList[b][1]:
                a += 1

            else:
                b += 1        

        return res