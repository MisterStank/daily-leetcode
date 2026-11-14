class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = -1

        for i in range(l,r+1):
            left = 0
            right = i
            current_sum = sum(nums[left:right])
            
            while True:
                if min_sum == -1 and current_sum > 0 :
                    min_sum = current_sum
                elif current_sum > 0 :
                    min_sum = min(min_sum,current_sum)

                if right == len(nums):
                    break
                
                current_sum = current_sum - nums[left] + nums[right]
                left += 1
                right += 1

        return min_sum
