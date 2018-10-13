"""推特OA
题目就是从句子里搜索给定关键词
思路是把所有词汇放进字典/哈希表，key是词汇，val是其所在句子
然后一个个query找
"""

def textQueries(sentences, queries):
    if (not sentences) or len(sentences)>10000:return 
    if (not queries) or len(queries)>10000:return 
    dic={}
    for i,s in enumerate(sentences):
        s=s.split()
        if (not s) or len(s)>10:return
        for word in s:
            if word not in dic:dic[word]=set([i])
            else:dic[word].add(i)
    for v in dic.values():if len(v)>10:return 
    for q in queries:
        q=q.split()
        if (not q) or len(q)>10:return 
        ans_i=set(range(len(sentences)))
        for word in q:
            if len(word)>11:return
            ans_i=ans_i&dic.get(word,set([]))
            if not ans_i:break
        if not ans_i:print(-1)
        else:
            for ans_i_ in sorted(ans_i):print(ans_i_,end=' ')
            print('\n',end='')