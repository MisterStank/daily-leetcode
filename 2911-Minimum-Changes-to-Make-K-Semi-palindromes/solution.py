class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        def get_cost(i, j):
            length = j - i + 1
            min_changes = INF

            for d in range(1, length):
                if length % d != 0:
                    continue

                changes = 0

                for offset in range(d):
                    left = i + offset
                    right = i + length - d + offset

                    while left < right:
                        if s[left] != s[right]:
                            changes += 1

                        left += d
                        right -= d

                min_changes = min(min_changes, changes)

            return min_changes

        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(i, j)

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for p in range(i - 1):
                    if dp[p][parts - 1] == INF:
                        continue

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[p][parts - 1] + cost[p][i - 1]
                    )

        return dp[n][k]
