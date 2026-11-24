# 1365. How Many Numbers Are Smaller Than the Current Number

[![LeetCode](https://img.shields.io/badge/LeetCode-1365-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

For each value in `nums`, count how many array elements are strictly smaller than it, and return those counts in an array.

## Example 1

```text
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
```

**Explanation:** There are four values smaller than `8`, none smaller than `1`, one smaller than each `2`, and three smaller than `3`.

## Example 2

```text
Input: nums = [6,5,4,8]
Output: [2,1,0,3]
```

## Example 3

```text
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
```

## Constraints

- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`
