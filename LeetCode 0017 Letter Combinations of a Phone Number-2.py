class Solution: # 63 99
    def letterCombinations(self, digits: str) -> List[str]:
        keyBoard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits: return []
        strs = [""]
        for d in digits:
            ns = []
            for c in keyBoard[d]:
                for s in strs:
                    ns.append(s+c)
            strs = ns
        return strs

