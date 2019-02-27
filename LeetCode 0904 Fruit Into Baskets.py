class Solution: #60%，很像LeetCode 159
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        ans = 0 #最大可能值
        categories = 0 #当前序列中水果种类
        visited = {} #当前水果按种类计数
        head = 0 #当前序列开头指针
        for tail, fruit in enumerate(tree): #当前序列结束指针，当前尾部新增水果种类
            if not visited.get(fruit, 0): #如果是新水果，则种类需要+1
                categories += 1
                visited[fruit] = 1
            else:
                visited[fruit] += 1 #从尾部增加
            while categories > 2: #要以合法的形式结束当前for-loop（水果种类不大于2），用while来保证
                justPopped = tree[head] #从头部弹出
                head += 1
                visited[justPopped] -= 1 #重新计算水果种类
                if not visited[justPopped]:
                    categories -= 1
            curLength = tail - head + 1 #更新最大可能值
            if curLength > ans: ans = curLength
        return ans
            
        