class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        c=0
        end=intervals[0][1]
        for i in intervals:
            if i[0]<end:
                c+=1
            else:
                end=i[1]
        return c-1