"""推特OA"""
def electionWinner(votes):
    box={}
    for vote in votes:
        if vote not in box:box[vote]=1
        else:box[vote]+=1
    maxer，maxlist=0,[]
    for name,vote in box.items():
        if vote>maxer:maxer,maxlist=vote,[name]
        elif vote==maxer:maxlist.append(name)
    return sorted(maxlist)[-1]