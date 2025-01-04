---
title: Args-Sample
date: 2025-01-04
author: Your Name
cell_count: 4
score: 0
---

```python

```


```python
def print_everything(*args):
        for count, thing in enumerate(args):
            print( '{0}. {1}'.format(count, thing))
```


```python
print_everything('apple', 'banana', 'cabbage', 'spinach')
```

    0. apple
    1. banana
    2. cabbage
    3. spinach



```python

```


---
**Score: 0**