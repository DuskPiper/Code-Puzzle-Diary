class Solution: # 55, 57
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = {}
        for n in arr:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
        
        ans = 0
        keys = list(counter.keys())
        for index, i in enumerate(keys): # ijk here are arr vals, not index;  so i<j<k is not guaranteed here
            for j in keys[index :]:
                k = target - i - j
                if k in counter:
                    if i == j == k: # case 1, all numbers are equal -> n(n-1)(n-2)/6
                        ans += counter[i] * (counter[i] - 1) * (counter[i] - 2) // 6
                    elif i == j: # case 2, 2 numbers are equal (any sequence) -> n(n-1)/2 * m
                        ans += counter[i] * (counter[i] - 1) // 2 * counter[k]
                    elif i < k and j < k: # case 3, all are diff -> m*n*o
                        ans += counter[i] * counter[j] * counter[k]
                        
        return ans % (10**9 + 7)
                    
            