class Solution(object): # 68%， 100%
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        get_head = {} # 哈希字典，用于从三角的两个脚快速查可能的顶点
        for triple in allowed: # 初始化字典
            if triple[:2] not in get_head: get_head[triple[:2]] = [triple[2]]
            else: get_head[triple[:2]].append(triple[2])
            
        def cur_layer_construct(floor): # 递归
            if len(floor) <= 1: return True # 堆叠到顶则回True
            possible_ceilings = [""] # 本层所有可能的天花板（上一层的地板），这个list的元素长度会从左到右逐渐长长
            for ptr in range(len(floor) - 1): # 从左到右根据地板铺天花板，每步铺一块天花板，天花板最终位数比地板少一位
                last_ceilings = list(possible_ceilings) # 上次循环的可能天花板，这次作为基础、往右修一块砖
                possible_ceilings = set([]) # 本次往右修好了一块砖的天花板的所有可能
                for head in get_head.get(floor[ptr] + floor[ptr + 1], []): # 本次往右修一块的所有可能性
                    possible_ceilings.update([former + head for former in last_ceilings]) # 右边的list是上次所有可能性append本次本种可能的砖
                if not possible_ceilings: return False # 本次往右没可能修了那就返回False
            for ceiling in possible_ceilings: # DFS，逻辑上是any(recursion for ceiling)，但直接这样写是BFS，费运行时间
                if cur_layer_construct(ceiling): return True
            return False
        
        return cur_layer_construct(bottom)