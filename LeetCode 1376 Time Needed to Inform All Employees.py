class Solution: # 22, 29
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        reports = defaultdict(list)
        for employee, mgr in enumerate(manager):
            reports[mgr].append(employee)
        
        
        def timeToInformAllReports(mgr): 
            if not reports[mgr]:
                return 0
            else:
                return informTime[mgr] + max([timeToInformAllReports(report) for report in reports[mgr]])
            
        return timeToInformAllReports(headID)