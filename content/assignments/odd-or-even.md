---
title: Odd-Or-Even
date: 2025-01-03
author: Your Name
cell_count: 7
score: 5
---

Nov 20 2024

Write a Python program that checks if a given number is odd or even.


```python
def check_odd_or_even(input_number):

    if input_number % 2 == 0:
        return f"{input_number} is Even"

    return f"{input_number} is Odd"
```


```python
check_odd_or_even(7)
```




    '7 is Odd'




```python
check_odd_or_even(8)
```




    '8 is Even'




```python
check_odd_or_even(0)
```




    '0 is Even'




```python
check_odd_or_even(-1)
```




    '-1 is Odd'




```python

```


---
**Score: 5**