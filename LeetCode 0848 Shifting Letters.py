class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        if not S:return ""
        form,ch,chdic,s=[],'a',{},''#form和dic是准备来在最后一步方便查表的
        for i in range(26):
            form.append(ch)
            chdic[ch]=i#chdic是一个字母-位序查找表
            ch=chr(ord(ch)+1)
        form*=2#form是一个52长的位序-字母查找表
        shifts[-1]=shifts[-1]%26
        for scan in range(len(shifts)-2,-1,-1):shifts[scan]=(shifts[scan]+shifts[scan+1])%26#换算成每一位需要shift的次数，避免多次重复shift
        for i,sh in enumerate(shifts):s+=form[chdic[S[i]]+sh]#逐个查表
        return s