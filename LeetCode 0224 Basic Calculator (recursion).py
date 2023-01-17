class Solution: # 5, 5
    def calculate(self, s: str) -> int:
    
        def calc(s: str) -> int:
            symbol = 1
            res = 0
            curNum = 0
            i = 0
            while i < len(s):
                c = s[i]
                if c in '0123456789':
                    curNum = curNum * 10 + int(c)
                elif c in '+-':
                    res += curNum * symbol
                    curNum = 0
                    symbol = 1 if c == '+' else -1
                elif c == '(':
                    closingIndex = findClosing(s, i)
                    curNum = calc(s[i+1 : closingIndex])
                    i = closingIndex
                i += 1
            res += curNum * symbol
            return res

        def findClosing(s: str, start: int) -> int:
            openCount = 0
            for i in range(start, len(s), 1):
                if s[i] == '(':
                    openCount += 1
                elif s[i] == ')':
                    openCount -= 1
                    if openCount == 0:
                        return i
            return -1

        return calc(s)
