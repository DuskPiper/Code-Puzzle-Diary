class Solution: # 54, 11
    def canTransform(self, start: str, end: str) -> bool:
        # L/R只能分别左/右移，且只能跨越X不能跨越其他L/R。L/R数量也不会增减。
        # 因此只需对比L和R出现顺序和次数相同、且一一对应的两个L或两个R，其左右位置是正确的(start的L不能在end中对应的L的左边，因为L只能左移)
        startFeature = [(v, i) for i, v in enumerate(start) if v == 'L' or v == 'R']
        endFeature = [(v, i) for i, v in enumerate(end) if v == 'L' or v == 'R']
        
        if len(startFeature) != len(endFeature):
            return False
        for (s, si), (e, ei) in zip(startFeature, endFeature):
            if s != e:
                return False
            if s == 'L' and si < ei:
                return False
            if s == 'R' and si > ei:
                return False
        return True