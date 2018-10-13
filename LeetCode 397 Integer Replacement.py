class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        思路是寻找pattern，考虑可以用recursion实现
        话说有个更好的节约空间的数学解法，我看不懂
		另外有个好的思路：在recursion中使用字典/哈希表记忆已有ir(k)数值，可以提高效率
        """
        if n<2:return 0
        def ir(n):
            if n==2:return 1
            elif n%2==0: return ir(n/2)+1
            else: return min(ir(n+1),ir(n-1))+1#造成树状分支，输入数字大了会托后腿
        return ir(n)