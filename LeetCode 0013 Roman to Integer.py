class Solution: # 26, 76
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if s[i] == 'M':
                ans += 1000
            elif s[i] == 'D':
                ans += 500
            elif s[i] == 'C':
                if i < len(s) - 1 and s[i+1] in ('D', 'M'):
                    ans -= 100
                else:
                    ans += 100
            elif s[i] == 'L':
                ans += 50
            elif s[i] == 'X':
                if i < len(s) - 1 and s[i+1] in ('L', 'C'):
                    ans -= 10
                else:
                    ans += 10
            elif s[i] == 'V':
                ans += 5
            else:
                if i < len(s) - 1 and s[i+1] in ('V', 'X'):
                    ans -= 1
                else:
                    ans += 1
                    
        return ans
                    
        