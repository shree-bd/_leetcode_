class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}  # ball -> color
        color_freq = {}  # color -> frequency
        result = []

        for ball, color in queries:
            # if ball was alrrady assigned a color, reduce old color count
            if ball in ball_color:
                old_color = ball_color[ball]
                color_freq[old_color] -= 1

                if color_freq[old_color] == 0:
                    del color_freq[old_color] # remove color if count is 0

            # assign new color to the ball
            ball_color[ball] = color

            # increase the count of the new color
            if color in color_freq:
                color_freq[color] += 1
            else:
                color_freq[color] = 1

            # append the number of unique colors
            result.append(len(color_freq))

        return result
        

# Time Complexity: O(N)
# Space Complexity: O(N)