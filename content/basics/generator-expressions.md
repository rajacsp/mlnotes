---
title: Generator-Expressions
date: 2024-12-14
author: Your Name
cell_count: 8
score: 5
---

---
title: "Generator Expressions Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
abc = [6, 8, 23, 2, 19]
```


```python
abc
```




    [6, 8, 23, 2, 19]




```python
result = [x for x in abc if(x > 6)]
```


```python
result
```




    [8, 23, 19]




```python
square = [x*x for x in result]
```


```python
square
```




    [64, 529, 361]




```python
# More expressions can be found here: https://www.python.org/dev/peps/pep-0289/
```


---
**Score: 5**