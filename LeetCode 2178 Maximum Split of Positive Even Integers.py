class Solution: # 11, 100
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        ans = [2]
        curSum = 2
        while curSum <= finalSum:
            curSum += ans[-1] + 2
            ans.append(ans[-1] + 2)
        
        curSum -= ans.pop(-1)
        ans[-1] += finalSum - curSum
        
        return ans
        