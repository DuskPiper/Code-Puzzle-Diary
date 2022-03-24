class Solution: # 85 77
    def decodeString(self, s: str) -> str:
        digits = '0123456789'
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        
        def helper(s):
            ans = ''
            num = 0
            child = ''
            unclosedBrasket = 0
            for c in s:
                if unclosedBrasket:
                    if c == ']' and unclosedBrasket == 1:
                        ans += helper(child) * num
                        child = ''
                        num = 0
                        unclosedBrasket = 0
                    else:
                        child += c
                        unclosedBrasket += c == '['
                        unclosedBrasket -= c == ']'
                else:
                    if c == '[':
                        unclosedBrasket += 1
                    elif c in digits:
                        num = num * 10 + int(c)
                    else:
                        ans += c
            return ans
        
        return helper(s)