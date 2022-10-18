class Solution:  # 31, 22
    def countRectangles(self, rect: List[List[int]], points: List[List[int]]) -> List[int]:
        rect.sort()
        heightsToWidths = {}  # heights -> [widths]
        for w, h in rect:
            if h not in heightsToWidths:
                heightsToWidths[h] = [w]
            else:
                heightsToWidths[h].append(w)
              
        heights = sorted(heightsToWidths.keys())
        ans = [0] * len(points)
        
        for i, (x, y) in enumerate(points):
            for h in heights[bisect.bisect_left(heights, y):]:   # binary search for enough heights
                ans[i] += (len(heightsToWidths[h]) - bisect.bisect_left(heightsToWidths[h], x))   # binary search for enough widths of each height
                
        return ans