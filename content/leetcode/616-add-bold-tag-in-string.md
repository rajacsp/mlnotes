---
title: 616-Add-Bold-Tag-In-String
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/add-bold-tag-in-string


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
  def addBoldTag(self, s: str, words: List[str]) -> str:
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
new Solution().addBoldTag()
```


---
**Score: 5**