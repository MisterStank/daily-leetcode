# 1524. Number of Sub-arrays With Odd Sum

[![LeetCode](https://img.shields.io/badge/LeetCode-1524-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-ffc01e)

Given an array of integers `arr`, return the number of subarrays with an odd sum. Since the answer can be very large, return it modulo `10^9 + 7`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Example 1

```text
Input: arr = [1,3,5]
Output: 4
```

**Explanation:**

All subarrays with an odd sum are `[1]`, `[1, 3, 5]`, `[3]`, and `[5]`.

## Example 2

```text
Input: arr = [2,4,6]
Output: 0
```

**Explanation:**

All subarrays have an even sum, so there are no subarrays with an odd sum.

## Example 3

```text
Input: arr = [1,2,3,4,5,6,7]
Output: 16
```

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 100`
