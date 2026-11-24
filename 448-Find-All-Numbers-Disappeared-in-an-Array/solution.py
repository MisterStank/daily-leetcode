class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = []
        set_nums = set(nums)
        for num in range(1,len(nums)+1):
            if num not in set_nums:
                ans.append(num)
        return ans