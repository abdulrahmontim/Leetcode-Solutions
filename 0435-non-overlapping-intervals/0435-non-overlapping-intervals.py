class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        intervals.sort(key = lambda interval: interval[0])
        
        last = intervals[0]
        for start, end in intervals[1:]:
           if start < last[1]:
                count += 1
                last[1] = min(last[1], end)
           else:
               last = [start, end]
        
        return count
        