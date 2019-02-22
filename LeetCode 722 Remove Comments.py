class Solution(object): # 100%, 17%
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_block = False # 状态标记，当前是否在/**/内部
        ans = [] # 答案，我试过了，如果不用list而用string、到最后再split的话，会节省很多内存，但是很费运行时间
        line_buffer = '' # 当前行的有效句子
        for line in source:
            length_ = len(line) - 1 # length - 1 避免重复计算
            i = 0 # iterator
            while i <= length_:
                if line[i] == '/' and i < length_ and line[i + 1] == '/' and not in_block: # '//'
                    break # 检测到行注视，直接跳出本行循环
                elif line[i] == '/' and i < length_ and line[i + 1] == '*' and not in_block: # '/*'
                    in_block = True # 设置block状态为True，现在开始在/**/内部
                    i += 2 # 一定要+2，避免/*/干扰
                elif line[i] == '*' and i < length_ and line[i + 1] == '/' and in_block: # '*/'
                    in_block = False # 结束/**/状态
                    i += 2 # 避免*/*干扰
                else: # 正常读值状态
                    if not in_block: line_buffer += line[i]
                    i += 1
            if line_buffer and not in_block: # 本行循环结束，如果本行不为空且目前不在/**/内部
                ans.append(line_buffer)
                line_buffer = '' # 答案换行，清空buffer，重起新行
        return ans