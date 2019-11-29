class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            hashset.add(local.replace('.','') + '@' + domain)
        return len(hashset)