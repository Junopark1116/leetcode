class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for i in range(len(emails)):
            splitidx = emails[i].index('@')
            local = emails[i][0:splitidx]
            domain = emails[i][splitidx:]
            local = local.replace('.', '')
            if '+' in local:
                local = local[0: local.index('+')]
            address = local + domain
            res.add(address)  
        return (len(res))
