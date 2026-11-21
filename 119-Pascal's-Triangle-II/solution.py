class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = [[1]]
        for i in range(1,rowIndex+1):
            pascal = [1]
            for j in range(len(dp[i-1])-1):
                pascal.append(dp[i-1][j]+dp[i-1][j+1])
            pascal.append(1)
            dp.append(pascal)
        return dp[rowIndex]
