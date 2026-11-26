# 3360. Stone Removal Game

[![LeetCode](https://img.shields.io/badge/LeetCode-3360-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/stone-removal-game/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

Alice and Bob alternate turns removing stones. Alice starts by removing 10 stones, then Bob removes 9, Alice removes 8, and so on, decreasing the required removal count by 1 after each turn.

A player who cannot remove the required number of stones loses. Return `true` if Alice wins, or `false` otherwise.

## Example 1

```text
Input: n = 12
Output: true
```

**Explanation:** Alice removes 10 stones, leaving 2. Bob cannot remove 9 stones, so Alice wins.

## Example 2

```text
Input: n = 1
Output: false
```

**Explanation:** Alice cannot remove 10 stones, so Alice loses.

## Constraints

- `1 <= n <= 50`
