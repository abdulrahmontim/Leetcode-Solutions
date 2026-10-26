class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = list()
        merged = False

        for interval in intervals:
            if newInterval[0] > interval[1]:
                res.append(interval)

            elif newInterval[1] < interval[0]:
                if not merged:
                    res.append(newInterval)
                    merged = True
                res.append(interval)
            
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        if not merged:
            res.append(newInterval)
            
        return res

        