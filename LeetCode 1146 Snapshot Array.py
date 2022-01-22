class SnapshotArray(object): # 24%, 94%

    def __init__(self, length):
        """
        :type length: int
        """
        self.ver = 0
        self.l = {} # Map<Index, List<Tuple[Version, Value]>>

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index not in self.l:
            self.l[index] = [(self.ver, val)]
        elif self.l[index][-1][0] == self.ver: # New value assigned under same version, update to latest
            self.l[index][-1] = (self.ver, val)
        else: # Record a new version-value pair
            self.l[index].append((self.ver, val))

    def snap(self):
        """
        :rtype: int
        """
        self.ver += 1
        return self.ver - 1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        if index not in self.l: # No val nor version
            return 0
        versions = self.l[index] # List<(Ver, Val)>
        if snap_id < versions[0][0]: 
            return 0
        elif snap_id > versions[-1][0]:
            return versions[-1][1]
        # Binary search
        left, right, knownMax = 0, len(versions) - 1, 0
        while left <= right:
            mid = (left + right) // 2
            if snap_id == versions[mid][0]:
                return versions[mid][1]
            elif snap_id > versions[mid][0]:
                knownMax = mid
                left = mid + 1
            else:
                right = mid - 1
        return versions[knownMax][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)