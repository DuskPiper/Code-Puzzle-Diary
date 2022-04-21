class Solution: # 85, 17
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        lh, rh = 0, 0
        while l < r:
            lh, rh = height[l], height[r]
            minHeight = min(lh, rh)
            area = max(area, minHeight * (r - l))
            if lh < rh:
                l += 1 # Need this for below "while" to make sense
                while height[l] < lh: 
                    l += 1
            else:
                r -= 1
                while height[r] < rh:
                    r -= 1
        return area
                