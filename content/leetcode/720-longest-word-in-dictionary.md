---
title: 720-Longest-Word-In-Dictionary
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-word-in-dictionary


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
  def longestWord(self, words: List[str]) -> str:
    root = {}

    for word in words:
      node = root
      for c in word:
        if c not in node:
          node[c] = {}
        node = node[c]
      node['word'] = word

    def dfs(node: dict) -> str:
      ans = node['word'] if 'word' in node else ''

      for child in node:
        if 'word' in node[child] and len(node[child]['word']) > 0:
          childWord = dfs(node[child])
          if len(childWord) > len(ans) or (len(childWord) == len(ans) and childWord < ans):
            ans = childWord

      return ans

    return dfs(root)
```


```
new Solution().longestWord()
```


---
**Score: 5**