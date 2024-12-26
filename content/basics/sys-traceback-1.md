---
title: Sys-Traceback-1
date: 2024-12-26
author: Your Name
cell_count: 8
score: 5
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==0.21.0
    



```python
import traceback
```


```python
def divide_numbers(a, b):
    return a / b
```


```python
try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except Exception:
    print("An error occurred!")
    # raise  # Reraises the exception to show the traceback
    print(traceback.format_exc())
```

    An error occurred!
    Traceback (most recent call last):
      File "/tmp/ipykernel_567376/663402224.py", line 2, in <module>
        result = divide_numbers(10, 0)
                 ^^^^^^^^^^^^^^^^^^^^^
      File "/tmp/ipykernel_567376/2831072420.py", line 2, in divide_numbers
        return a / b
               ~~^~~
    ZeroDivisionError: division by zero
    



```python

```


```python

```


---
**Score: 5**