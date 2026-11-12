class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_inc = 0
        max_dec = 0
        count_inc = 0
        count_dec = 0
        
        #increasing loop
        for i in range(len(nums)):
            if i == 0:
                count_inc += 1
                max_inc = max(max_inc,count_inc)
            elif nums[i] > nums[i-1]:
                count_inc += 1
                max_inc = max(max_inc,count_inc)
            else:
                max_inc = max(max_inc,count_inc)
                count_inc = 1

        #decreasing loop
        for i in range(len(nums)):
            if i == 0:
                count_dec += 1
                max_dec = max(max_dec,count_dec)
            elif nums[i] < nums[i-1]:
                count_dec += 1
                max_dec = max(max_dec,count_dec)
            else:
                max_dec = max(max_dec,count_dec)
                count_dec = 1

        return max(max_inc,max_dec)
