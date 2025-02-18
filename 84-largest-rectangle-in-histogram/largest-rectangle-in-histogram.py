class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # stores (index, height)
        max_area = 0
        # n = len(heights)

        # for i in range(n+1):
        #     h = heights[i] if i < n else 0

        #     while stack and heights[stack[-1]] > h:
        #         height = heights[stack.pop()]
        #         width = i if not stack else i - stack[-1] - 1
        #         max_area = max(max_area, height * width)

        #     stack.append(i)

        # return max_area

        # Iterate through heights with an extra bar at the end to process remaining stack
        for i, h in enumerate(heights + [0]):  
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]  # Pop height
                width = i if not stack else i - stack[-1] - 1  # Compute width
                max_area = max(max_area, height * width)  # Update max area
            stack.append(i)  # Push current index into stack

        return max_area  


# Time Complexity: O(N)
# Space Complexity: O(N)