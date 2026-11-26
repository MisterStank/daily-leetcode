# 845. Longest Mountain in Array

[![LeetCode](https://img.shields.io/badge/LeetCode-845-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/longest-mountain-in-array/description/)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-ffc01e)

Given an integer array `arr`, return the length of the longest subarray that is a mountain array. A mountain array has at least three elements and is strictly increasing before a peak, then strictly decreasing after the peak. Return `0` if no mountain subarray exists.

## Example 1

```text
Input: arr = [2,1,4,7,3,2,5]
Output: 5
```

**Explanation:** The largest mountain is `[1,4,7,3,2]`, which has length `5`.

## Example 2

```text
Input: arr = [2,2,2]
Output: 0
```

**Explanation:** There is no mountain subarray.

## Constraints

- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 10^4`

## Follow up

- Can you solve it using only one pass?
- Can you solve it in `O(1)` space?
