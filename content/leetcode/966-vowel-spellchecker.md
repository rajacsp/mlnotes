---
title: 966-Vowel-Spellchecker
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/vowel-spellchecker


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
  def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
    def lowerKey(word: str) -> str:
      return '$' + ''.join([c.lower() for c in word])

    def vowelKey(word: str) -> str:
      return ''.join(['*' if c.lower() in 'aeiou' else c.lower() for c in word])

    ans = []
    dict = {}

    for word in wordlist:
      dict.setdefault(word, word)
      dict.setdefault(lowerKey(word), word)
      dict.setdefault(vowelKey(word), word)

    for q in queries:
      if q in dict:
        ans.append(dict[q])
      elif lowerKey(q) in dict:
        ans.append(dict[lowerKey(q)])
      elif vowelKey(q) in dict:
        ans.append(dict[vowelKey(q)])
      else:
        ans.append('')

    return ans
```


```
new Solution().spellchecker()
```


---
**Score: 5**