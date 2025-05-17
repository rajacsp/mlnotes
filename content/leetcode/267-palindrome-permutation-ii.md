---
title: 267-Palindrome-Permutation-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/palindrome-permutation-ii


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
class Solution:
  def generatePalindromes(self, s: str) -> List[str]:
    # Get character occurrence
    count = Counter(s)

    # Count odd one
    odd = sum(value & 1 for value in count.values())

    # can't form any palindrome
    if odd > 1:
      return []

    ans = []
    candidates = []
    mid = ''

    # Get mid and candidates characters
    for key, value in count.items():
      if value & 1:
        mid += key
      for _ in range(value // 2):
        candidates.append(key)

    # Generate all unique palindromes from candidates
    def dfs(used: List[bool], path: List[chr]) -> None:
      if len(path) == len(candidates):
        ans.append(''.join(path) + mid + ''.join(path[::-1]))
        return

      for i, candidate in enumerate(candidates):
        if used[i]:
          continue
        if i > 0 and candidate == candidates[i - 1] and not used[i - 1]:
          continue
        used[i] = True
        path.append(candidate)
        dfs(used, path)
        path.pop()
        used[i] = False

    # Backtracking to generate our ans (strings)
    dfs([False] * len(candidates), [])
    return ans
```


```
new Solution().generatePalindromes()
```


---
**Score: 5**