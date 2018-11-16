class Solution: #96%
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        validEmails = set([])
        for email in emails:
            domain, addr = email.split('@')
            domain = domain.replace('.','')
            plusIndex = domain.find('+')
            if plusIndex > 0:
                domain = domain[:plusIndex]
            validEmails.add(domain + addr)
        return len(validEmails)
            