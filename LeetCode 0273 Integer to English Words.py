class Solution:  # 29, 39
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        
        self.digitMap = {
            "0": "Zero",
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine"
        }
        
        self.teensMap = {
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen"
        }
        
        self.tensMap = {
            "1": "Ten",
            "2": "Twenty",
            "3": "Thirty",
            "4": "Forty",
            "5": "Fifty",
            "6": "Sixty",
            "7": "Seventy",
            "8": "Eighty",
            "9": "Ninety"
        }
        
        self.unitsMap = {
            0: "",
            1: "Thousand",
            2: "Million",
            3: "Billion",
            4: "Trillion",
            5: "Quadrillion",
            6: "Quintillion",
            7: "Sextillion",
            8: "Septillion",
            9: "Octillion",
            10: "Nonillion",
            11: "Decillion"
        }
        
        
        def getChunkName(s):
            while len(s) < 3:
                s = "0" + s
            ans = []
            if s[0] != '0':
                ans.append(self.digitMap[s[0]])
                ans.append("Hundred")
            if s[1] != '0':
                if s[1] == '1':
                    ans.append(self.teensMap[s[1:]])
                    return ans
                else:
                    ans.append(self.tensMap[s[1]])
            if s[2] != '0':
                ans.append(self.digitMap[s[2]])
            return ans
        
        ans = []
        chunkStack = []
        while num:
            chunkStack.append(str(num % 1000))
            num = num // 1000
        for i, chunk in enumerate(chunkStack):
            chunkName = getChunkName(chunk)
            if chunkName: 
                chunkName.append(self.unitsMap[i])
            ans = chunkName + ans
            
        return " ".join(ans).strip()
        
                    
                    