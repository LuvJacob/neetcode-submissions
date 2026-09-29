class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack holds indices of bars with increasing heights
        stack = []
        best = 0

        # Add a 0-height bar at the end to "flush" the stack
        for i in range(len(heights) + 1):
            curr_height = heights[i] if i < len(heights) else 0

            # If current bar is smaller, we've found the RIGHT boundary
            # for bars that are taller than curr_height.
            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]

                # After popping, stack[-1] is the index of the previous smaller bar
                left_smaller_index = stack[-1] if stack else -1

                # The current index i is the first smaller bar on the right
                width = i - left_smaller_index - 1

                best = max(best, h * width)

            stack.append(i)

        return best