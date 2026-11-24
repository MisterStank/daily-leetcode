# 268. Missing Number

[![LeetCode](https://img.shields.io/badge/LeetCode-268-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/missing-number/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in that range missing from the array.

## Example 1

```text
Input: nums = [3,0,1]
Output: 2
```

**Explanation:** `n = 3`, so all numbers are in the range `[0,3]`. `2` is the missing number.

## Example 2

```text
Input: nums = [0,1]
Output: 2
```

**Explanation:** `n = 2`, so all numbers are in the range `[0,2]`. `2` is the missing number.

## Example 3

```text
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

**Explanation:** `n = 9`, so all numbers are in the range `[0,9]`. `8` is the missing number.

## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are unique.

**Follow up:** Implement a solution using only `O(1)` extra space and `O(n)` runtime.
