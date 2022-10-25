class Solution: # 80 69
    def largestRectangleArea(self, heights: List[int]) -> int:
        previousLows = [-1]  # mono stack, ascending
        ans = 0
        heights.append(0)
        for i in range(len(heights)):
            while previousLows and heights[previousLows[-1]] > heights[i]:
                h = heights[previousLows.pop()]   # construct a rect for the previous high bar
                w = i - previousLows[-1] - 1 if previousLows else 1   # the rect's right border is "i", bcz we know heights[i] is smaller; left border is the new previousLows[-1] bcz it's the "previous"Low of the newly popped element
                ans = max(ans, h * w)
            previousLows.append(i)
        return ans
            