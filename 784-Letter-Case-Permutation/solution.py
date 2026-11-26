class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                output.append(sub)
            else:
                backtrack(sub+s[i],i+1)
                if s[i].isalpha():
                    backtrack(sub+s[i].swapcase(),i+1)
                
        output = []
        backtrack()
        return output