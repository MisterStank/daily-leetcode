from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        ops = 0
        left = len(nums) - 1
        dq = deque()

        for right in range(len(nums)-1, -1, -1):
            num = nums[right]
            cnt = 1

            while dq and dq[-1][0] < num:
                val, c = dq.pop()
                cnt += c
                ops += (num - val) * c

            dq.append((num, cnt))

            while ops > k:
                val, c = dq.popleft()
                ops -= val - nums[left]
                left -= 1

                if c > 1:
                    dq.appendleft((val, c-1))

            count += left - right + 1

        return count
