class Solution:
	def solution(D, A):
		ans = []
		for num in A:
			for _ in range(D - 1):
				if num == -1: break
				num = A[num]
			ans.append(num)
		return ans		
