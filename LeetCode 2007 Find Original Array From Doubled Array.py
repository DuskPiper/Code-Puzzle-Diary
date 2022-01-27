class Solution(object):
    def findOriginalArray(self, changed): # 31%, 24%
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        res = []
        counter = Counter(changed)
        if counter[0] % 2 == 1: # Corner case: odd amount of "0"
            return []
        for n in sorted(changed, key = lambda x: abs(x)):
            if counter[n] == 0: # n was previously popped out with n/2
                continue
            if counter[2 * n] == 0: # No 2n match
                return []
            res.append(n)
            counter[n] -= 1 # pop n
            counter[2 * n] -= 1 # pop 2n
        return res