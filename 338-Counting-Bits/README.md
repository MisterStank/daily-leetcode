# 338. Counting Bits

[![LeetCode](https://img.shields.io/badge/LeetCode-338-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/counting-bits/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

Given an integer `n`, return an array `ans` of length `n + 1` where for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1` bits in the binary representation of `i`.

## Example 1

```text
Input: n = 2
Output: [0,1,1]
```

**Explanation:** `0` has `0` ones, `1` has `1` one, and `2` has `1` one.

## Example 2

```text
Input: n = 5
Output: [0,1,1,2,1,2]
```

**Explanation:** `0`, `1`, `10`, `11`, `100`, and `101` contain `0`, `1`, `1`, `2`, `1`, and `2` ones respectively.

## Constraints

- `0 <= n <= 10^5`

**Follow up:** It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?
