class Node: # TrieNode
    def __init__(self, char: str):
        self.char = char
        self.times = 0
        self.children = {}
        self.end = False

class AutocompleteSystem: # 63, 82
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node('')
        self.cur = self.root
        self.userInput = ''
        for s, t in zip(sentences, times):
            self.add(s, t)
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.add(self.userInput, 1)
            self.cur = self.root
            self.userInput = ''
            return []
        
        self.userInput += c
        return self.search(self.userInput)

    def add(self, s: str, times: int):
        cur = self.root
        for c in s:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.end = True
        cur.times += times

    def search(self, sentence: str) -> list:
        node = self.root
        for c in sentence:
            node = node.children.get(c)
            if not node:
                return []
        res = [] # [(sentence, times)]
        self.getSentencesHelper(node, '', res)
        #print(res)
        top3 = sorted(res, key=lambda x: (-x[1], x[0]))[:3]
        return list(map(lambda x: sentence[:-1] + x[0], top3))

    def getSentencesHelper(self, node: Node, ancestors: str, res: list):
        s = ancestors + node.char
        if node.end:
            res.append((s, node.times))
        for child in node.children.values():
            self.getSentencesHelper(child, s, res)
        


        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)