# 700. Search in a Binary Search Tree

[![LeetCode](https://img.shields.io/badge/LeetCode-700-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)
![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)

You are given the root of a binary search tree and an integer `val`. Find the node whose value equals `val` and return the subtree rooted at that node. If no such node exists, return `null`.

## Example 1

```text
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```

## Example 2

```text
Input: root = [4,2,7,1,3], val = 5
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[1, 5000]`
- `1 <= Node.val <= 10^7`
- `root` is a binary search tree
- `1 <= val <= 10^7`
