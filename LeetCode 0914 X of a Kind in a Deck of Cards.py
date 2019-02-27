class Solution:
    def hasGroupsSizeX(self, deck):
        """
        放进counter，然后找数目的最大公约数，大于1则True
        """
        c=collections.Counter(deck)
        for i in range(min(c.values()),0,-1):#从大往小试公约数，第一个遇到的是最大公约数
            if all(map(lambda x:x%i==0,c.values())):break#用map和all提升速度
        return True if i>1 else False#最大公约数即是group大小，>1则True
        
        