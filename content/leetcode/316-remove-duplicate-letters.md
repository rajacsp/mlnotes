---
title: 316-Remove-Duplicate-Letters
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-duplicate-letters


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
  def removeDuplicateLetters(self, s: str) -> str:
    ans = []
    count = Counter(s)
    used = [False] * 26

    for c in s:
      count[c] -= 1
      if used[ord(c) - ord('a')]:
        continue
      while ans and ans[-1] > c and count[ans[-1]] > 0:
        used[ord(ans[-1]) - ord('a')] = False
        ans.pop()
      ans.append(c)
      used[ord(ans[-1]) - ord('a')] = True

    return ''.join(ans)
```


```
new Solution().removeDuplicateLetters()
```


---
**Score: 5**