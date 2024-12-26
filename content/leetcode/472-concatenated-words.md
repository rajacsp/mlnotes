---
title: 472-Concatenated-Words
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/concatenated-words


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
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    wordSet = set(words)

    @functools.lru_cache(None)
    def isConcat(word: str) -> bool:
      for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
          return True

      return False

    return [word for word in words if isConcat(word)]
```


```
new Solution().findAllConcatenatedWordsInADict()
```


---
**Score: 5**