---
title: 929-Unique-Email-Addresses
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/unique-email-addresses


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
  def numUniqueEmails(self, emails: List[str]) -> int:
    seen = set()

    for email in emails:
      local, domain = email.split('@')
      local = local.split('+')[0].replace('.', '')
      seen.add(local + '@' + domain)

    return len(seen)
```


```
new Solution().numUniqueEmails()
```


---
**Score: 5**