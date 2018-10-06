#思路：用哈希表/字典，即可进行单次扫描
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:return False
        dic = {}
		for i,v in enumerate(nums):
		if v in dic:return [dic[v],i]
		dic[target-v]=i
