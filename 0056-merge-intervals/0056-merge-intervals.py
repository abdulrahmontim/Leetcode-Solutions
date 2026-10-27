class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = list()
        
        intervals.sort(key=lambda interval: interval[0])
        
        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
        
        