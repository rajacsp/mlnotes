---
title: 1081-Smallest-Subsequence-Of-Distinct-Characters
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/smallest-subsequence-of-distinct-characters


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
  def smallestSubsequence(self, text: str) -> str:
    ans = []
    count = Counter(text)
    used = [False] * 26

    for c in text:
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
new Solution().smallestSubsequence()
```


---
**Score: 5**