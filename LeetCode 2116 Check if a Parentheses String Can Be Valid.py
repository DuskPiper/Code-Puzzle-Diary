class Solution(object): # 6, 33
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        # scan
        flexibles = 0
        openings = 0
        closings = 0
        for i, c in enumerate(s):
            if locked[i] == '0':
                flexibles += 1
            else:
                openings += int(c == '(')
                closings += int(c == ')')
            if flexibles + openings < closings:
                return False
            
        # reverse scan
        flexibles = 0
        openings = 0
        closings = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                flexibles += 1
            else:
                openings += int(s[i] == '(')
                closings += int(s[i] == ')')
            if flexibles + closings < openings:
                return False
        return True
            
        