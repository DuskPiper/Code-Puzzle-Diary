class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
		是一个递归的问题（但是可以用迭代代码实现
		对于n的答案，其实是对n-1的答案的演绎，对n-1每个元素都进行以下两种操作之一：
		1.在整个外面套一层()
		2.在每个可能的slot(其实是所有length内所有下标)插入一个()
		由此可以得到n的答案
		以空string "" 为n=0的答案，由此可以递归演绎到n的答案
        """
        ans,i=set([""]),0
        while i<n:
            ans_lo=ans.copy()
            ans=set()
            for x in ans_lo:
                ans.add("("+x+")")
                for j in range(len(x)):
                    ans.add(x[:j]+"()"+x[j:])
            i+=1
        return list(ans)