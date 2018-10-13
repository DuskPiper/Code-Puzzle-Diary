"""推特的OA"""
def missingWords(s, t):
    # Write your code here
    s=s.split(' ')
    t=t.split(' ')
    #print(s)
    #print(t)
    ans=[]
    while s:
        word=s.pop(0)
        if word!=t[0]:ans.append(word)
        else:t.pop(0)
        if not t:return ans+s
    return ans+s