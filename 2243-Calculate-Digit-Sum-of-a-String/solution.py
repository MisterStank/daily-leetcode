class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            tmp = ""

            for i in range(0,len(s),k):
                tmp_sum = 0
                for j in range(min(k, len(s) - i)):
                    tmp_sum += int(s[j+i])
                tmp += str(tmp_sum)
            
            s = tmp[:]
        return s
