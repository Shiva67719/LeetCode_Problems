class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        d=[]
        for i in range(len(matrix)):
            d.extend(matrix[i])
            d.sort()
        return d[k-1]
