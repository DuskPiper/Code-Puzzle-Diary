def solution(s):
	ans = 0
	head = 0
	charType = 0
	visited = {}
	for i in range(ord(a), ord(z) + 1): visited[chr(i)] = 0 #dic, dic[a~z]=0
	for tail, char in enumerate(s): #head and tail are two pointers
		visited[char] += 1
		if not visited[char]: charType += 1
		while charType > 2: #stop when meat need: no more than 2 chars
			visited[s[head]] -= 1
			if not visited[s[head]]: charType -= 1
			head += 1
		curLength = tail - head + 1
		if curLength > ans: ans = curLength #Update if greater
	return ans