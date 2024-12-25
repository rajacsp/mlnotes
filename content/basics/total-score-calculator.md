---
title: Total-Score-Calculator
date: 2024-12-25
author: Your Name
cell_count: 7
score: 5
---

```python

```


```python
import random
```


```python
total_score_list = []
for i in range(6):

    current_score = random.randint(0, 6)

    print(f'ball {i}, current score: {current_score}')
    total_score_list.append(current_score)
```

    ball 0, current score: 3
    ball 1, current score: 0
    ball 2, current score: 5
    ball 3, current score: 1
    ball 4, current score: 5
    ball 5, current score: 3



```python
total_score_list
```




    [3, 0, 5, 1, 5, 3]




```python
total_score_int = 0
for i in range(6):

    current_score = random.randint(0, 6)

    print(f'ball {i}, current score: {current_score}')
    total_score_int += current_score
```

    ball 0, current score: 4
    ball 1, current score: 6
    ball 2, current score: 1
    ball 3, current score: 5
    ball 4, current score: 6
    ball 5, current score: 5



```python
total_score_int
```




    27




```python

```


---
**Score: 5**