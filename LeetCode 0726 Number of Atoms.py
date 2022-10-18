class Solution: # 86 60
    def countOfAtoms(self, formula: str) -> str:
        
        self.digits = "0123456789"
        self.lowercase = "qwertyuiopasdfghjklzxcvbnm"
        self.i = 0
        self.f = formula
        
        def parseFragment():
            counter = {}
            while self.i < len(self.f):
                if self.f[self.i] == '(':
                    self.i += 1
                    cnt, mlt = parseFragment()
                    for key, val in cnt.items():
                        updateCounter(counter, key, val*mlt)
                elif self.f[self.i] == ')':
                    self.i += 1
                    if self.i < len(self.f) and self.f[self.i] in digits:
                        multiplier = parseNumber()
                    else:
                        multiplier = 1
                    return counter, multiplier
                elif self.f[self.i] not in digits:  # at Atom
                    atom = parseAtom()
                    if self.i < len(self.f) and self.f[self.i] in digits:
                        num = parseNumber()
                    else:
                        num = 1
                    updateCounter(counter, atom, num)
            return counter, 1
                    
        def parseNumber():
            j = self.i
            while j < len(self.f) and self.f[j] in digits:
                j += 1
            num = int(self.f[self.i:j])
            self.i = j
            return num
        def parseAtom():
            j = self.i + 1
            while j < len(self.f) and self.f[j] in self.lowercase:
                j += 1
            atom = self.f[self.i:j]
            self.i = j
            return atom
        def updateCounter(counter, key, val):
            if key not in counter:
                counter[key] = 0
            counter[key] += val

        count, _ = parseFragment()
        
        ans = ""
        for key in sorted(count.keys()):
            ans += key
            if count[key] > 1:
                ans += str(count[key])
                
        return ans
        