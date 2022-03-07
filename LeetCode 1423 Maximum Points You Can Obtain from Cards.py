class Solution: # 95, 41
    def maxScore(self, cardPoints: List[int], k: int) -> int: # Sliding window
        windowSum = sum(cardPoints[:k]) # initial window
        length = len(cardPoints)
        ans = windowSum
        for windowOffset in range(1, k + 1, 1):
            windowSum = windowSum - cardPoints[k - windowOffset] + cardPoints[length - windowOffset]
            ans = max(ans, windowSum)
        return ans