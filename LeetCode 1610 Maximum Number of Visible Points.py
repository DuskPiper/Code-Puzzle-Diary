class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int: # 36%, 89%
        # 把点转换成相对角度
        locX, locY = location
        angles = []
        numTargetsAtViewerLocation = 0 # corner case，目标与观测者重合，永远可见
        for x, y in points:
            if x == locX and y == locY:
                numTargetsAtViewerLocation += 1
            else:
                angleInRad = math.atan2(y - locY, x - locX)
                a = angleInRad * 180 / math.pi
                if a < 0:
                    a += 360
                angles.append(a)
        # 排序，倍长
        angles.sort()
        angles += [a + 360 for a in angles]
        # sliding window   
        mostViewable = 0
        lIndex = 0
        for rIndex in range(len(angles) // 2):
            rAngle = angles[rIndex]
            while angles[lIndex] - rAngle <= angle:
                lIndex += 1
            curViewable = lIndex - rIndex
            mostViewable = max(mostViewable, curViewable)
        
        return mostViewable + numTargetsAtViewerLocation
        