class Solution(object): # 56, 56
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        tasks.sort(reverse=True)
        ans = [len(tasks)] # worst case answer. Using list to avoid global variable update error, it doesn't really function as list
        sessions = [] # Total time of each session
        
        def dfs(i):
            if len(sessions) > ans[0]: 
                return
            if i == len(tasks): # Already fit in all tasks, new i is out of bound
                ans[0] = min(ans[0], len(sessions))
                return
            
            task = tasks[i]
            
            # Fit into existing session
            for si, s in enumerate(sessions):
                if s + task <= sessionTime: # can fit
                    sessions[si] += task
                    dfs(i + 1) # try next task
                    sessions[si] -= task
            # Create a new session for this task
            sessions.append(task)
            dfs(i + 1)
            sessions.pop(-1)
            
        dfs(0)
        return ans[0]