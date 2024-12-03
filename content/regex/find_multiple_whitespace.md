---
title: Find Multiple Whitespace
date: 2024-12-04
author: Your Name
cell_count: 9
score: 5
---

---
title: "Find Multiple Whitespace"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import re
```


```python
help(re.split)
```

    Help on function split in module re:
    
    split(pattern, string, maxsplit=0, flags=0)
        Split the source string by the occurrences of the pattern,
        returning a list containing the resulting substrings.  If
        capturing parentheses are used in pattern, then the text of all
        groups in the pattern are also returned as part of the resulting
        list.  If maxsplit is nonzero, at most maxsplit splits occur,
        and the remainder of the string is returned as the final element
        of the list.
    



```python
re.split(r'\s{2,}', "2012.03.04       check everything      status: OK")
```




    ['2012.03.04', 'check everything', 'status: OK']




```python
content = "2012.03.04       check everything      status: OK"
```


```python
content
```




    '2012.03.04       check everything      status: OK'




```python
list = re.split(r'\s{2,}', content)
```


```python
for a in list:
    print(a)
```

    2012.03.04
    check everything
    status: OK



```python

```


---
**Score: 5**