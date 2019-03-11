class Solution(object):
    def trap(self, height): # 74, 40
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) <= 2:
            return 0
        water = [0 for _ in range(len(height))]
        # scan left -> right
        water[0] = height[0]
        for i in range(1, len(height)):
            water[i] = max(water[i - 1], height[i])
        water[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            water[i] = min(water[i], max(water[i + 1], height[i]))
        return sum(water) - sum(height)
        # possible improvement: two pointers from both sides to mid, start with the side with smaller val