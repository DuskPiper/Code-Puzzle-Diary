class Solution: # 74, 63
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return str(x) == str(x)[::-1]
            