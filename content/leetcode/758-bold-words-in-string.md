---
title: 758-Bold-Words-In-String
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/bold-words-in-string


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
  def boldWords(self, words: List[str], s: str) -> str:
    n = len(s)
    ans = []
    # bold[i] := True if s[i] should be bolded
    bold = [0] * n

    boldEnd = -1  # s[i:boldEnd] should be bolded
    for i in range(n):
      for word in words:
        if s[i:].startswith(word):
          boldEnd = max(boldEnd, i + len(word))
      bold[i] = boldEnd > i

    # Construct the with bold tags
    i = 0
    while i < n:
      if bold[i]:
        j = i
        while j < n and bold[j]:
          j += 1
        # s[i:j] should be bolded
        ans.append('<b>' + s[i:j] + '</b>')
        i = j
      else:
        ans.append(s[i])
        i += 1

    return ''.join(ans)
```


```
new Solution().boldWords()
```


---
**Score: 5**