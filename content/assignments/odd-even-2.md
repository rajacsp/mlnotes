---
title: Odd-Even-2
date: 2024-11-24
author: Your Name
cell_count: 7
score: 5
---

```python

```


```python

```


```python
def odd_even():
    for i in range(10):      
        if i % 2 == 0:
              print(f"The number {i} is even")
        else:
            print(f"The number {i} is odd")
```


```python
odd_even()
```

    The number 0 is even
    The number 1 is odd
    The number 2 is even
    The number 3 is odd
    The number 4 is even
    The number 5 is odd
    The number 6 is even
    The number 7 is odd
    The number 8 is even
    The number 9 is odd



```python
def odd_even(input_val):

    if input_val %2 == 0:
        return f"The number {input_val} is even"
    
    return f"The number {input_val} is odd"
```


```python
for i in range(10):   
    print(odd_even(i))
```

    The number 0 is even
    The number 1 is odd
    The number 2 is even
    The number 3 is odd
    The number 4 is even
    The number 5 is odd
    The number 6 is even
    The number 7 is odd
    The number 8 is even
    The number 9 is odd



```python

```


---
**Score: 5**