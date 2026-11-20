class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 0

        for num in nums:
            if num in dp:
                dp[num + 1] = dp[num] + 1
            else:
                dp[num + 1] = 1

            if num - 1 in dp:
                dp[num] = dp[num - 1] + 1
            else:
                dp[num] = 1

            ans = max(ans, dp[num], dp[num + 1])

        return ans