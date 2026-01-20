class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split("@")

            clean = " "
            for ch in local:
                if ch == '+':
                    break
                if ch != '.':
                    clean += ch

            unique.add(clean + "@" + domain)
        return len(unique)