---
title: 804-Unique-Morse-Code-Words
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/unique-morse-code-words


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
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    transformations = set()

    for word in words:
      transformation = ''.join(morse[ord(c) - ord('a')] for c in word)
      transformations.add(transformation)

    return len(transformations)
```


```
new Solution().uniqueMorseRepresentations()
```


---
**Score: 5**