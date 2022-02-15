class Solution: # 56%, 98%
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for t in tokens:
            if t not in "+-*/":
                numStack.append(int(t))
            else:
                n1 = numStack.pop(-1)
                n0 = numStack.pop(-1)
                res = None
                if t == "+": res = n0 + n1
                elif t == "-": res = n0 - n1
                elif t == "*": res = n0 * n1
                else: res = int(float(n0) / n1)
                numStack.append(res)
        return numStack[-1]
        