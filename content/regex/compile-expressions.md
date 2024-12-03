---
title: Compile-Expressions
date: 2024-12-04
author: Your Name
cell_count: 5
score: 5
---

```python
import re
```


```python
# precompile regex patterns
regex_entries = [
    re.compile(p)
    for p in ['awesome', 'ocean']
]
```


```python
content = 'Duckduck go is awesome and it is getting better everyday'

print('Text : {!r}'.format(content))
```

    Text : 'Duckduck go is awesome and it is getting better everyday'



```python
for regex in regex_entries:
    print('Finding  {} -> '.format(regex.pattern), end = ' ')

    if(regex.search(content)):
        print('matched')
    else:
        print('not matched')
```

    Finding  awesome ->  matched
    Finding  ocean ->  not matched



```python

```


---
**Score: 5**