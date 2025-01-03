---
title: 792-Number-Of-Matching-Subsequences
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-matching-subsequences


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
  def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    root = {}

    def insert(word: str) -> None:
      node = root
      for c in word:
        if c not in node:
          node[c] = {'count': 0}
        node = node[c]
      node['count'] += 1

    for word in words:
      insert(word)

    def dfs(s: str, i: int, node: dict) -> int:
      ans = node['count'] if 'count' in node else 0

      if i >= len(s):
        return ans

      for c in string.ascii_lowercase:
        if c in node:
          try:
            index = s.index(c, i)
            ans += dfs(s, index + 1, node[c])
          except ValueError:
            continue

      return ans

    return dfs(s, 0, root)
```


```
new Solution().numMatchingSubseq()
```


---
**Score: 5**