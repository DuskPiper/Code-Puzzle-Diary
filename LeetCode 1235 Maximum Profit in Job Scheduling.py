class Solution: # 75, 87
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1]) # sort by endTime
        dp = [jobs[0][2]] # "max profit if ending at i-th endTime"
        for job in jobs[1:]:
            # 2 options: do or not do this job
            #   1,do
            #     Find most recent history task that has no conflict
            i = len(dp) - 1
            while i >= 0 and jobs[i][1] > job[0]:
                i -= 1
            profitsIfDoThisJob = dp[i] + job[2] if i >= 0 else job[2]
            #   2, not do
            profitsIfNotDoThisJob = dp[-1]
            
            dp.append(max(profitsIfDoThisJob, profitsIfNotDoThisJob))
        return dp[-1]