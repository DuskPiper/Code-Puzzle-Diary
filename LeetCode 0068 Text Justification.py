class Solution(object):
    
    def fullJustify(self, words, maxWidth): # 67%, 25%
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # Step 1 Greedy divide
        lines = []
        lineWidth = []
        curLen, curLine = 0, []
        for word in words:
            if curLen + len(curLine) + len(word) <= maxWidth: # append to curLine
                curLine.append(word)
                curLen += len(word)
            else: # curLine full, start new line
                lines.append(curLine[:])
                lineWidth.append(curLen)
                curLine = [word]
                curLen = len(word)
        if curLine:
            lines.append(curLine)
            lineWidth.append(curLen)
            
        # Step 2 Format each line
        output = []
        for ln in range(len(lines) - 1):
            line = lines[ln]
            totalSpaces = maxWidth - lineWidth[ln]
            if (len(line) == 1): # Corner case: 1 word in line
                output.append(line[0] + ' ' * totalSpaces)
                continue
            totalIntervals = len(line) - 1
            baseSpaceLen = totalSpaces // totalIntervals
            numExtraLenSpaces = totalSpaces % totalIntervals
            print(totalSpaces, totalIntervals, baseSpaceLen, numExtraLenSpaces)
            strBdr = line[0]
            for i in range(1, len(line)):
                strBdr += ' ' * (baseSpaceLen + int(i <= numExtraLenSpaces))
                strBdr += line[i]
            output.append(str(strBdr))
        lastLine = ' '.join(lines[-1])
        output.append(lastLine + ' ' * (maxWidth - len(lastLine)))
        return output