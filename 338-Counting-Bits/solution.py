class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        lastpowoftwo = 2
        for i in range(n+1):
            if i == 0: ans.append(0)
            elif i == 1: ans.append(1)
            elif i == 2: ans.append(1)
            elif i == lastpowoftwo * 2:
                ans.append(1)
                lastpowoftwo *= 2
            else:
                ans.append(ans[lastpowoftwo] + ans[i-lastpowoftwo])
        return ans