class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_name = {}

        # Step 1: Setup parents and name map
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)  # Union all emails in same account

        # Step 2: Group emails by root parent
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # Step 3: Build result
        result = []
        for root in groups:
            result.append([email_to_name[root]] + sorted(groups[root]))
        return result
        