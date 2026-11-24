class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            t = target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == t: return [i,j]
        return []