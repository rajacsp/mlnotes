---
title: Fibonacci-1
date: 2024-12-25
author: Your Name
cell_count: 16
score: 15
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("scipy"))
```

    scipy==1.14.1
    



```python
def get_fib(n):

    if n <= 1

    return 0
```


```python
get_fib(5)
```




    0




```python
# 5 = 5 + 4 + 3 + 2 +1 = 
```


```python
def fibonacci(n):
    if n == 0 or n == 1: return n
    else: return fibonacci(n-1)+fibonacci(n-2)
```


```python
fibonacci(5)
```

    n: 5
    n: 4
    n: 3
    n: 2
    n: 1
    n: 0
    n: 1
    n: 2
    n: 1
    n: 0
    n: 3
    n: 2
    n: 1
    n: 0
    n: 1





    5




```python
def fibonacci_for_loop(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
```


```python
fibonacci_for_loop(5)
```

    0 1 1 2 3 


```python
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```


```python
n = 10
fib_sequence = [fibonacci_recursive(i) for i in range(n)]
print(fib_sequence)
```

    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



```python
n = 5
fib_sequence = [fibonacci_recursive(i) for i in range(n)]
print(fib_sequence)
```

    [0, 1, 1, 2, 3]



```python

```


```python
def fibonacci_loop(n):
    result_list = []
    
    a, b = 0, 1

    # print(f'first: a: {a}, b:{b}')
    for _ in range(n):
        result_list.append(a)
        a, b = b, a + b

        # print(f'second: a: {a}, b: {b}')
        print(f'result_list: {result_list}')
        
    return result_list

n = 5  # Change this number for more terms
print(fibonacci_loop(n))
```

    result_list: [0]
    result_list: [0, 1]
    result_list: [0, 1, 1]
    result_list: [0, 1, 1, 2]
    result_list: [0, 1, 1, 2, 3]
    [0, 1, 1, 2, 3]



```python

```


---
**Score: 15**