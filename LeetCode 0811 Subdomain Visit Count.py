class Solution:  # 21 17
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)
            domains = domain.split('.')
            if not domains: 
                continue
            domainBuilder = domains.pop()
            if domainBuilder not in counter: counter[domainBuilder] = 0
            counter[domainBuilder] += count
            while domains:
                domainBuilder = domains.pop() + '.' + domainBuilder
                if domainBuilder not in counter: counter[domainBuilder] = 0
                counter[domainBuilder] += count
                
        ans = []
        for entry in counter.items():
            ans.append(str(entry[1]) + ' ' + entry[0])
        return ans