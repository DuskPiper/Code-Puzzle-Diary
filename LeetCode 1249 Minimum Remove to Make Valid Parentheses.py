class Solution(object): # 81, 73
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = list(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else: # No more '(' in stock, remove current extra ')'
                    s[i] = ''
        for i in stack:
            s[i] = '' # remove extra '('
        return ''.join(s)