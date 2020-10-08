class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # split local and domain
        # split local on + and take first part
        # remove . in remaining
        # join all and add to set
        
        emailsSet = set()
        
        for email in emails:
            localName, domain = email.split('@')
            localName = localName.split('+')[0]
            parsedEmail = "".join(localName.split('.') + ['@', domain])
            emailsSet.add(parsedEmail)
            
        # print(emailsSet)
        return len(emailsSet)