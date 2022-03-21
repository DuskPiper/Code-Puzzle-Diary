class Node:
    def __init__(self, typ, name):
        self.type = typ
        self.name = name
        self.children = {}
        self.content = ""

class FileSystem: # 55, 69
    
    def __init__(self):
        self.root = Node("dir", "_root")
        

    def ls(self, path: str) -> List[str]:
        paths = path[1:].split("/") if path != "/" else []
        ptr = self.root
        for p in paths:
            ptr = ptr.children[p]
        if ptr.type == "file":
            return [ptr.name]
        else:
            return sorted(map(lambda node: node.name, ptr.children.values()))
            

    def mkdir(self, path: str) -> None:
        paths = path[1:].split("/") if path != "/" else []
        ptr = self.root
        for p in paths:
            if p not in ptr.children:
                ptr.children[p] = Node("dir", p)
            ptr = ptr.children[p]
                

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath[1:].split("/") if path != "/" else []
        ptr = self.root
        for p in paths[:-1]:
            if p not in ptr.children:
                ptr.children[p] = Node("dir", p)
            ptr = ptr.children[p]
        fileName = paths[-1]
        if fileName not in ptr.children:
            ptr.children[fileName] = Node("file", fileName)
        file = ptr.children[fileName]
        file.content += content

    def readContentFromFile(self, filePath: str) -> str:
        paths = filePath[1:].split("/") if path != "/" else []
        ptr = self.root
        for p in paths:
            ptr = ptr.children[p]
        return ptr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)