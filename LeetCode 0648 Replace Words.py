class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
		用预先截取好的方法，避免重复截取词汇，毕竟截取很费时间
        """
        sent=sentence.split(' ')
        lendict=set()
        lensent={}
        for root in dict:lendict.add(len(root))
        for l in lendict:
            lensent[l]=[word[:l] for word in sent]#预先截取好
        for root in sorted(dict,key=lambda x:len(x),reverse=True):
            s=lensent[len(root)]
            for i,word in enumerate(s):
                if word==root:
                    sent[i]=root
        return " ".join(sent)
            
        
        