class Solution: # 71, 90
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        
        def getApproaches(targetSeconds):
            minute = targetSeconds // 60
            second = targetSeconds % 60
            if targetSeconds < 60:
                return [[0, 0, second//10, second%10]]
            elif second >= 40:
                return [[minute//10, minute%10, second//10, second%10]]
            elif minute > 99:
                return [[(minute-1)//10, (minute-1)%10, (second+60)//10, (second+60)%10]]
            else:
                return [
                    [minute//10, minute%10, second//10, second%10],
                    [(minute-1)//10, (minute-1)%10, (second+60)//10, (second+60)%10]
                ]
            
        def getCost(approach, startAt, moveCost, pushCost):
            while(approach[0] == 0):
                approach.pop(0)
            finger = startAt
            cost = 0
            for digit in approach:
                if digit != finger:
                    cost += moveCost
                    finger = digit
                cost += pushCost
            return cost
        
        approaches = getApproaches(targetSeconds)
        print(approaches)
        costs = [getCost(approach, startAt, moveCost, pushCost) for approach in approaches]
        
        return min(costs)
            