class Solution: # 96 63
    def numSteps(self, s: str) -> int:
        carry = 0
        step = 0
        for i in xrange(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1: # odd, +1÷2 => carry 1 to upper level, and remove current level (0)
                carry = 1
                step += 2
            else: # even, ÷2 => remove current level (0)
                step += 1
        return step + carry
                