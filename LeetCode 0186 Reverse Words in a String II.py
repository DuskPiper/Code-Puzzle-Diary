class Solution: # 99 49
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        # Swap the s
        swap(0, len(s) - 1)
        
        # Swap each word
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                swap(start, i - 1)
                start = i + 1
            elif i == len(s) - 1:
                swap(start, len(s) - 1)

