# 1266. Minimum Time Visiting All Points

[![LeetCode](https://img.shields.io/badge/LeetCode-1266-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/minimum-time-visiting-all-points/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

There are `n` points with integer coordinates on a 2D plane. Return the minimum time in seconds needed to visit all points in the given order. Movement can be horizontal, vertical, or diagonal between coordinates.

## Example 1

```text
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
```

**Explanation:** One optimal path is `[1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]`. The time from `[1,1]` to `[3,4]` is 3 seconds, and the time from `[3,4]` to `[-1,0]` is 4 seconds.

## Example 2

```text
Input: points = [[3,2],[-2,2]]
Output: 5
```

## Constraints

- `points.length == n`
- `1 <= n <= 100`
- `points[i].length == 2`
- `-1000 <= points[i][0], points[i][1] <= 1000`
