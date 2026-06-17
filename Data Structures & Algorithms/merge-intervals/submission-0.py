class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(reverse=False, key=lambda x: x[0])
        n = len(intervals)
        results = []
        for i in range(0, n - 1, 1):
            if intervals[i][1] >= intervals[i+1][0]:
                max_end = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1][1] = max_end
                intervals[i+1][0] = intervals[i][0]
            else:
                results.append(intervals[i])
        results.append(intervals[-1])
        return results



            

 
        