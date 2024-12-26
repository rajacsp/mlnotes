---
title: 692-Top-K-Frequent-Words
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/top-k-frequent-words


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
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    ans = []
    bucket = [[] for _ in range(len(words) + 1)]

    for word, freq in Counter(words).items():
      bucket[freq].append(word)

    for b in reversed(bucket):
      for word in sorted(b):
        ans.append(word)
        if len(ans) == k:
          return ans
```


```
new Solution().topKFrequent()
```


---
**Score: 5**