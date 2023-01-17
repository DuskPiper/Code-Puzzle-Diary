class Solution: # 86 71
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rmax, cmax = len(maze), len(maze[0])
        visited = set([])
        q = [(start[0], start[1])]
        while q:
            r, c = q.pop()
            if r == destination[0] and c == destination[1]:
                return True
            visited.add((r, c))

            # Find where can we reach
            leftMost = c
            while leftMost > 0 and maze[r][leftMost - 1] == 0:
                leftMost -= 1

            rightMost = c
            while rightMost < cmax - 1 and maze[r][rightMost + 1] == 0:
                rightMost += 1

            upMost = r
            while upMost > 0 and maze[upMost - 1][c] == 0:
                upMost -= 1

            downMost = r
            while downMost < rmax - 1 and maze[downMost + 1][c] == 0:
                downMost += 1

            for x, y in ((r, leftMost), (r, rightMost), (upMost, c), (downMost, c)):
                if (x, y) not in visited:
                    q.append((x, y))
        return False