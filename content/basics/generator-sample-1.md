---
title: Generator-Sample-1
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

```python

```


```python
# Example: Loop through a generator and print its values
def sample_generator():
    for i in range(5):  # Generates numbers 0 to 4
        yield i
```


```python
gen = sample_generator()  # Create the generator
```


```python
gen
```




    <generator object sample_generator at 0x7fe180371000>




```python
for value in gen:  # Loop through the generator
    print(value)
```

    0
    1
    2
    3
    4



```python

```


---
**Score: 5**