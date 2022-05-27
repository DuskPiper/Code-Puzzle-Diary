class Solution: # 7, 35
    def intToRoman(self, num: int) -> str:
        ans = ''
        # > 1000
        if num // 1000:
            ans += 'M' * (num // 1000)
            num = num % 1000
            
        # > 100
        if num // 100:
            if num >= 900:
                ans += 'CM'
                num -= 900
            elif num >= 500:
                ans += 'D'
                num -= 500
                while num >= 100:
                    ans += 'C'
                    num -= 100
            elif num >= 400:
                ans += 'CD'
                num -= 400
            else:
                while num >= 100:
                    ans += 'C'
                    num -= 100
        
        # > 10
        if num // 10:
            if num >= 90:
                ans += 'XC'
                num -= 90
            elif num >= 50:
                ans += 'L'
                num -= 50
                while num >= 10:
                    ans += 'X'
                    num -= 10
            elif num >= 40:
                ans += 'XL'
                num -= 40
            else:
                while num >= 10:
                    ans += 'X'
                    num -= 10
        
        # > 1
        if num:
            if num == 9:
                ans += 'IX'
            elif num >= 5:
                ans += 'V'
                num -= 5
                while num:
                    ans += 'I'
                    num -= 1
            elif num == 4:
                ans += 'IV'
            else:
                while num:
                    ans += 'I'
                    num -= 1
        return ans
                
                