---
title: 591-Tag-Validator
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/tag-validator


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
  def isValid(self, code: str) -> bool:
    if code[0] != '<' or code[-1] != '>':
      return False

    containsTag = False
    stack = []

    def isValidCdata(s: str) -> bool:
      return s.find('[CDATA[') == 0

    def isValidTagName(tagName: str, isEndTag: bool) -> bool:
      nonlocal containsTag
      if not tagName or len(tagName) > 9:
        return False
      if any(not c.isupper() for c in tagName):
        return False

      if isEndTag:
        return stack and stack.pop() == tagName

      containsTag = True
      stack.append(tagName)
      return True

    i = 0
    while i < len(code):
      if not stack and containsTag:
        return False
      if code[i] == '<':
        # Inside a tag, so we can check if it's a cdata
        if stack and code[i + 1] == '!':
          closeIndex = code.find(']]>', i + 2)
          if closeIndex == -1 or not isValidCdata(code[i + 2:closeIndex]):
            return False
        elif code[i + 1] == '/':  # End tag
          closeIndex = code.find('>', i + 2)
          if closeIndex == -1 or not isValidTagName(code[i + 2:closeIndex], True):
            return False
        else:  # Start tag
          closeIndex = code.find('>', i + 1)
          if closeIndex == -1 or not isValidTagName(code[i + 1:closeIndex], False):
            return False
        i = closeIndex
      i += 1

    return not stack and containsTag
```


```
new Solution().isValid()
```


---
**Score: 5**