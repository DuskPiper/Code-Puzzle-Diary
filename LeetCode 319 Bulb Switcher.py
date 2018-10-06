'''拆解问题：寻找因数数量为奇数的元素个数
进一步：仅有完全平方数有奇数个因数，普通数都有偶数个（可以通过n=a*b的a,b对称性得）
问题翻译:寻找给定n内完全平方数个数'''
class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (int)Math.sqrt(n);