# 2911. Minimum Changes to Make K Semi-palindromes

[![LeetCode](https://img.shields.io/badge/LeetCode-2911-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/description/)
![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-ff6b6b)

Given a string `s` and an integer `k`, divide `s` into exactly `k` non-overlapping substrings, each with a length of at least `2`. Return the minimum number of character changes needed to make every substring a semi-palindrome.

A string is a semi-palindrome if its length has a proper divisor `d` such that the `d` sequences formed by taking characters at indices with the same remainder modulo `d` are all palindromes.

## Example 1

```text
Input: s = "bba", k = 1
Output: 1
```

**Explanation:**

Changing the first character produces `"aba"`, which is a palindrome and therefore a semi-palindrome.

## Example 2

```text
Input: s = "abba", k = 1
Output: 0
```

**Explanation:**

`"abba"` is already a palindrome, so no changes are needed.

## Constraints

- `2 <= k <= 100`
- `2 * k <= s.length <= 200`
- `s` consists only of lowercase English letters.
