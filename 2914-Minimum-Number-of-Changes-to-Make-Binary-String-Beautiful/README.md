# 2914. Minimum Number of Changes to Make Binary String Beautiful

[![LeetCode](https://img.shields.io/badge/LeetCode-2914-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-ffc01e)

You are given a binary string `s`. A string is beautiful if it can be partitioned into one or more substrings such that:

- Each substring has an even length.
- Each substring contains only `0`s or only `1`s.

In one operation, you can change a character in `s` to `0` or `1`. Return the minimum number of operations needed to make `s` beautiful.

## Example 1

```text
Input: s = "1001"
Output: 2
```

**Explanation:**

Change `s[1]` and `s[3]` to `0`. The string becomes `"0000"`, which can be partitioned into `"00"` and `"00"`.

## Example 2

```text
Input: s = "10"
Output: 1
```

**Explanation:**

Change one character so both characters are equal. The resulting string can be partitioned into one substring of even length.

## Constraints

- `2 <= s.length <= 10^5`
- `s.length` is even.
- `s[i]` is either `'0'` or `'1'`.
