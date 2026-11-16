# 2243. Calculate Digit Sum of a String

[![LeetCode](https://img.shields.io/badge/LeetCode-2243-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

You are given a string `s` consisting of digits and an integer `k`.

A *round* consists of:

1. Dividing `s` into consecutive groups of size `k`, with the last group allowed to be shorter than `k`.
2. Replacing each group with the sum of its digits, then concatenating the resulting sums to form a new string.

Repeat rounds until the resulting string has length less than or equal to `k`, then return it.

## Example 1

```text
Input: s = "11111222223", k = 3
Output: "135"
```

**Explanation:**

First round: `"111" + "112" + "222" + "23"` becomes `"3" + "4" + "6" + "5" = "3465"`.

Second round: `"346" + "5"` becomes `"13" + "5" = "135"`.

Since the resulting string has length `3`, which is less than or equal to `k`, return `"135"`.

## Example 2

```text
Input: s = "00000000", k = 3
Output: "000"
```

**Explanation:**

The first round produces `"000"`. Its length is less than or equal to `k`, so return `"000"`.

## Constraints

- `1 <= s.length <= 100`
- `2 <= k <= 100`
- `s` consists of digits.
