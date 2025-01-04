---
title: Seconds2Timeformat
date: 2025-01-04
author: Your Name
cell_count: 7
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

```


```python
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    result = []
    if hours > 0:
        result.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        result.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if remaining_seconds > 0 or not result:  # Always include seconds
        result.append(f"{remaining_seconds} second{'s' if remaining_seconds > 1 else ''}")

    return " ".join(result)
```


```python
print(format_time(224492))  # 62 hours 21 minutes 32 seconds
print(format_time(3760))    # 1 hour 2 minutes 40 seconds
print(format_time(3525))    # 58 minutes 45 seconds
print(format_time(78))      # 1 minute 18 seconds
```

    62 hours 21 minutes 32 seconds
    1 hour 2 minutes 40 seconds
    58 minutes 45 seconds
    1 minute 18 seconds



```python

```


---
**Score: 5**