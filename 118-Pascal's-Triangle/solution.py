class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = [[1]]
        for i in range(1,numRows):
            pascal = [1]
            for j in range(len(dp[i-1])-1):
                pascal.append(dp[i-1][j]+dp[i-1][j+1])
            pascal.append(1)
            dp.append(pascal)
        return dp
