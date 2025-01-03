---
title: 854-K-Similar-Strings
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/k-similar-strings


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
  def kSimilarity(self, s1: str, s2: str) -> int:
    ans = 0
    q = deque([s1])
    seen = {s1}

    while q:
      for _ in range(len(q)):
        curr = q.popleft()
        if curr == s2:
          return ans
        for child in self._getChildren(curr, s2):
          if child in seen:
            continue
          q.append(child)
          seen.add(child)
      ans += 1

    return -1

  def _getChildren(self, curr: str, target: str) -> List[str]:
    children = []
    s = list(curr)
    i = 0  # First index s.t. curr[i] != target[i]
    while curr[i] == target[i]:
      i += 1

    for j in range(i + 1, len(s)):
      if s[j] == target[i]:
        s[i], s[j] = s[j], s[i]
        children.append(''.join(s))
        s[i], s[j] = s[j], s[i]

    return children
```


```
new Solution().kSimilarity()
```


---
**Score: 5**