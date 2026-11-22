# 2124. Check if All A's Appears Before All B's

[![LeetCode](https://img.shields.io/badge/LeetCode-2124-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

Given a string `s` consisting only of the characters `'a'` and `'b'`, return `true` if every `'a'` appears before every `'b'` in the string.

Otherwise, return `false`.

## Example 1

```text
Input: s = "aaabbb"
Output: true
```

**Explanation:** Every `'a'` appears before every `'b'`.

## Example 2

```text
Input: s = "abab"
Output: false
```

**Explanation:** There is an `'a'` that appears after a `'b'`.

## Example 3

```text
Input: s = "bbb"
Output: true
```

**Explanation:** There are no `'a'` characters, so the condition is satisfied.

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is either `'a'` or `'b'`.
