---
name: leetcode-readme
description: Add or update a LeetCode problem README and register the problem in the repository progress table. Use when a user provides a LeetCode problem URL or asks to add README documentation for a problem solution.
---

# LeetCode README

Use this skill when adding README documentation for a LeetCode solution in this repository.

## Workflow

1. Parse the problem number and title slug from the LeetCode URL.
2. Inspect the matching solution folder. Folder names generally use the pattern `<problem-number>-<Problem-Title>`.
3. Inspect the existing solution file to confirm the problem's folder and public API.
4. Retrieve the official problem statement and examples from the LeetCode GraphQL API or the provided URL.
5. Create `<solution-folder>/README.md` if it does not exist.
6. Add the problem to the progress table in the repository root `README.md` if it is not already listed.
7. Validate Markdown formatting and run `git diff --check`.

## README format

Use this structure:

````markdown
# <problem number>. <problem title>

[![LeetCode](https://img.shields.io/badge/LeetCode-<problem number>-FFA116?logo=leetcode&logoColor=white)](<LeetCode problem description URL>)
![Difficulty: <Easy|Medium|Hard>](<difficulty badge URL>)

<Short restatement of the problem statement.>

## Example 1

```text
Input: ...
Output: ...
```

**Explanation:** <If the official statement provides an explanation, summarize it accurately.>

## Constraints

- `<constraint>`
````

Include additional examples as `Example 2`, `Example 3`, and so on.

Preserve important follow-up requirements or definitions in the README when present.

## Metadata and badges

- Easy: `![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-00b8a3)`
- Medium: `![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-ffc01e)`
- Hard: `![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-ff6b6b)`

## Fetching problem data

Use LeetCode GraphQL when direct page fetching is blocked:

```powershell
$body = @{
    query = 'query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId title difficulty content } }'
    variables = @{ titleSlug = '<title-slug>' }
} | ConvertTo-Json -Compress

Invoke-RestMethod -Uri 'https://leetcode.com/graphql' -Method Post -ContentType 'application/json' -UserAgent 'Mozilla/5.0' -Body $body
```

Do not copy copyrighted text unnecessarily. Summarize the problem faithfully and keep the examples and constraints accurate.

## Validation

Verify that:

- The README is in the folder containing `solution.py`.
- The title and problem number match the official problem.
- The examples match the official statement.
- The constraints use the repository's existing Markdown style.
- The root progress table contains exactly one entry for the problem.
- `git diff --check` reports no formatting errors.
