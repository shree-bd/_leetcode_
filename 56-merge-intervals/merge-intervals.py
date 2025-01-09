class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intevals based on the start times
        intervals.sort(key = lambda i : i[0])
        result = [intervals[0]]  # Initialize with the first interval

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]

            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result


            # [1,5], [2,4] = [1,5]
        