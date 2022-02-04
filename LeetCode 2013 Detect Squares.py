class DetectSquares(object): # 15%, 44%

    def __init__(self):
        self.points = collections.Counter() # count all points (points @ same x,y are treated differently)
        self.xToYs = collections.defaultdict(list) # all points x to its y
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.points[point[0], point[1]] += 1
        self.xToYs[point[0]].append(point[1])
        

    def count(self, p):
        """
        :type point: List[int]
        :rtype: int
        """
        ans = 0
        ys = self.xToYs[p[0]] # all points sharing same y with current p
        for y in ys:
            sideLen = abs(y - p[1])
            if sideLen == 0:
                continue
            # go left
            p2 = (p[0] - sideLen, p[1])
            p3 = (p[0] - sideLen, y)
            ans += self.points[p2] * self.points[p3]
            # go right
            p2 = (p[0] + sideLen, p[1])
            p3 = (p[0] + sideLen, y)
            ans += self.points[p2] * self.points[p3]
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
