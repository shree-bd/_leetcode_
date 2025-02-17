class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # stores (index, height)
        max_area = 0
        n = len(heights)

        for i in range(n+1):
            h = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area


# Time Complexity: O(N)
# Space Complexity: O(N)