class Solution:
	def filter(emailList):
		clean = set([])
		ans = set([])
		for email in emailList:
			local, domain = email.split('@')
			local = local.replace('.', '')
			plusIndex = local.find('+')
			if plusIndex >= 0:
				local = local[:plusIndex]
			if not local: continue #make sure the address is still valid
			cleanEmail = local + domain
			if cleanEmail in clean:
				ans.add(cleanEmail)
			else: clean.add(cleanEmail)
	return len(ans)