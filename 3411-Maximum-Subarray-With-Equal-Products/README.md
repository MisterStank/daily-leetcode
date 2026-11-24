# 3411. Maximum Subarray With Equal Products

[![LeetCode](https://img.shields.io/badge/LeetCode-3411-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/maximum-subarray-with-equal-products/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

You are given an array of positive integers `nums`.

An array `arr` is called **product equivalent** if:

```text
prod(arr) == lcm(arr) * gcd(arr)
```

Here:

- `prod(arr)` is the product of all elements of `arr`.
- `gcd(arr)` is the greatest common divisor of all elements of `arr`.
- `lcm(arr)` is the least common multiple of all elements of `arr`.

Return the length of the longest product equivalent subarray of `nums`.

## Example 1

```text
Input: nums = [1,2,1,2,1,1,1]
Output: 5
```

**Explanation:** The longest product equivalent subarray is `[1,2,1,1,1]`, where `prod = 2`, `gcd = 1`, and `lcm = 2`.

## Example 2

```text
Input: nums = [2,3,4,5,6]
Output: 3
```

**Explanation:** The longest product equivalent subarray is `[3,4,5]`.

## Example 3

```text
Input: nums = [1,2,3,1,4,5,1]
Output: 5
```

## Constraints

- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 10`
