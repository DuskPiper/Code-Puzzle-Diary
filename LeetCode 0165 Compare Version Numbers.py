class Solution(object): # 99.9% Time, 92% RAM
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        lmax = max(len(v1), len(v2))
        while len(v1) < lmax: v1.append("0")
        while len(v2) < lmax: v2.append("0")
        for i in xrange(lmax):
            vi1 = int(v1[i])
            vi2 = int(v2[i])
            if vi1 > vi2: return 1
            if vi1 < vi2: return -1
        return 0