---
title: 411-Minimum-Unique-Word-Abbreviation
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-unique-word-abbreviation


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
  def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
    m = len(target)

    def getMask(word: str) -> int:
      # mask[i] = 0 := target[i] == word[i]
      # mask[i] = 1 := target[i] != word[i]
      # E.g. target = "apple"
      #        word = "blade"
      #        mask =  11110
      mask = 0
      for i, c in enumerate(word):
        if c != target[i]:
          mask |= 1 << m - 1 - i
      return mask

    masks = [getMask(word) for word in dictionary if len(word) == m]
    if not masks:
      return str(m)

    abbrs = []

    def getAbbr(cand: int) -> str:
      abbr = ''
      replacedCount = 0
      for i, c in enumerate(target):
        if cand >> m - 1 - i & 1:
          # cand[i] = 1, abbr should show the original character
          if replacedCount:
            abbr += str(replacedCount)
          abbr += c
          replacedCount = 0
        else:
          # cand[i] = 0, abbr can be replaced
          replacedCount += 1
      if replacedCount:
        abbr += str(replacedCount)
      return abbr

    # For all candidate representation of target
    for cand in range(2**m):
      # All masks have at lease one bit different from candidate
      if all(cand & mask for mask in masks):
        abbr = getAbbr(cand)
        abbrs.append(abbr)

    def getAbbrLen(abbr: str) -> int:
      abbrLen = 0
      i = 0
      j = 0
      while i < len(abbr):
        if abbr[j].isalpha():
          j += 1
        else:
          while j < len(abbr) and abbr[j].isdigit():
            j += 1
        abbrLen += 1
        i = j
      return abbrLen

    return min(abbrs, key=lambda x: getAbbrLen(x))
```


```
new Solution().minAbbreviation()
```


---
**Score: 5**