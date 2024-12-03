---
title: Simple-Regex
date: 2024-12-03
author: Your Name
cell_count: 3
score: 0
---

---
title: "Simple Regex"
author: "Raja CSP Raman"
date: 2019-04-29
description: "-"
type: technical_note
draft: false
---

```python
import re
```


```python
pattern = 'awesome'

content = 'Duckduck go is awesome and it is getting better everyday'

match = re.search(pattern, content)

#print(match)

start = match.start()
end = match.end()

#print(match.string)

print(start, end)
```

    15 22



---
**Score: 0**