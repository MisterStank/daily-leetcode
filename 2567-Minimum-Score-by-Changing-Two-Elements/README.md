# 2567. Minimum Score by Changing Two Elements

[![LeetCode](https://img.shields.io/badge/LeetCode-2567-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-ffc01e)

You are given a **0-indexed** integer array `nums`.

In one operation, you can increase or decrease `nums[i]` by `1`.

In at most two operations, change the value of at most two elements of `nums`. The score of `nums` is defined as `max(nums) - min(nums)`.

Return the minimum score possible after changing at most two elements.

## Example 1

```text
Input: nums = [1,4,3]
Output: 0
```

**Explanation:**

Change `1` to `3` and `4` to `3`. The resulting array is `[3, 3, 3]`, so the score is `3 - 3 = 0`.

## Example 2

```text
Input: nums = [1,4,7,8,10]
Output: 3
```

**Explanation:**

Change `1` to `4` and `10` to `7`. The resulting array is `[4, 4, 7, 8, 7]`, so the score is `8 - 4 = 4`. Alternatively, change `7` to `8` and `8` to `7`, giving a score of `3`.

## Constraints

- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
