class SparseVector: # 86, 31
    def __init__(self, nums: List[int]):
        self.map = {}
        self.key = [] # index
        for i, n in enumerate(nums):
            if n != 0:
                self.map[i] = n
                self.key.append(i)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        i, j = 0, 0
        while i < len(self.key) and j < len(vec.key):
            if self.key[i] == vec.key[j]:
                ans += self.map[self.key[i]] * vec.map[vec.key[j]]
                i += 1
                j += 1
            elif self.key[i] < vec.key[j]:
                i += 1
            else:
                j += 1
        return ans
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)