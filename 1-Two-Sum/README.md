# 1. Two Sum

[![LeetCode](https://img.shields.io/badge/LeetCode-1-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/two-sum/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

Given an integer array `nums` and an integer `target`, return the indices of two numbers whose sum is `target`. There is exactly one solution, and you cannot use the same element twice. Return the indices in any order.

## Example 1

```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`.

## Example 2

```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Explanation:** `nums[1] + nums[2] = 2 + 4 = 6`.

## Example 3

```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Explanation:** `nums[0] + nums[1] = 3 + 3 = 6`.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

**Follow up:** Can you design an algorithm with time complexity less than `O(n^2)`?
