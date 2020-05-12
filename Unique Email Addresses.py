class Solution(object):
    def CheckLocalname(self, email):

        temp = email.split('@')
        localname, domain = temp[0], temp[1]
        plus_indx = localname.find('+')
        if plus_indx != -1:
            localname = localname[:plus_indx]
        localname = localname.replace('.','')

        return localname + "@" + domain

    def numUniqueEmails(self, emails):

        for i in range(0,len(emails)):
            emails[i] = Solution.CheckLocalname(self, emails[i])

        uniqu_eemails = set(emails)
        result = len(uniqu_eemails)

        return result

print(Solution.numUniqueEmails(0,[ "test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com" ]))
print(Solution.numUniqueEmails(0,["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))