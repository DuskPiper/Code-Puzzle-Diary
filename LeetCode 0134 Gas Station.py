class Solution(object): # 22, 5
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gain = [g - c for g, c in zip(gas, cost)] # Each gas gain
        tank = 0
        ans = 0
        if sum(gain) < 0: return -1
        for i, g in enumerate(gain):
            tank += g # cumulate gains
            if tank < 0: # starting from cur "ans" won't make it
                tank = 0 # reset
                ans = i + 1 # try next possible staring point
        if ans >= len(gas): ans = -1 # no possible starting point
        return ans
