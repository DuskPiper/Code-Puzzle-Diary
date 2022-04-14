class Solution(object): # 53, 9
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path += '/'
        l = []
        builder = ''
        i = 0
        while i < len(path):
            c = path[i]
            if c == '/':
                if builder:
                    l.append(str(builder))
                    builder = ''
                i += 1
            elif c == '.' and not builder:
                if path[i:i+2] == './':
                    i += 2
                elif path[i:i+3] == '../':
                    i += 3
                    if l:
                        l.pop()
                else:
                    i += 1
                    builder += c
            else:
                i += 1
                builder += c
        if builder:
            l.append(builder)
        return '/' + '/'.join(l)
            