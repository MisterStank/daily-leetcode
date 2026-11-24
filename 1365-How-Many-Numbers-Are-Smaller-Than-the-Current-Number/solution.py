class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        sorted_nums = sorted(nums)
        for i,num in enumerate(nums):
            ans.append(sorted_nums.index(num))
        return ans 