---
title: 30-Substring-With-Concatenation-Of-All-Words
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/substring-with-concatenation-of-all-words


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
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    if len(s) == 0 or words == []:
      return []

    k = len(words)
    n = len(words[0])
    ans = []
    count = Counter(words)

    for i in range(len(s) - k * n + 1):
      seen = defaultdict(int)
      j = 0
      while j < k:
        word = s[i + j * n: i + j * n + n]
        seen[word] += 1
        if seen[word] > count[word]:
          break
        j += 1
      if j == k:
        ans.append(i)

    return ans
```


```
new Solution().findSubstring()
```


---
**Score: 5**