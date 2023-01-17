class Solution: # 90 65
    def reorderSpaces(self, text: str) -> str:
        numSpaces = text.count(" ")
        words = text.split()
        if len(words) == 1: return words[0] + " " * numSpaces
        spaceSize = numSpaces // (len(words) - 1)
        extraSpaces = numSpaces % (len(words) - 1)
        return (" " * spaceSize).join(words) + (" " * extraSpaces)
