---
title: Pint-1
date: 2025-01-03
author: Your Name
cell_count: 16
score: 15
---

```python
# Created: 20250103
```


```python
# https://pypi.org/project/Pint/0.24.4/
```


```python
# !pip install pint
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
print(pyu.ps2("requests pint"))
```

    requests==2.32.3
    pint==0.24.4
    



```python

```


```python
import pint
```


```python
ureg = pint.UnitRegistry()
```


```python
distance = 100 * ureg.meters
```


```python
distance
```




100 meter




```python
time = 10 * ureg.seconds
```


```python
time
```




10 second




```python
speed = distance / time
```


```python
speed
```




10.0 meter/second




```python
speed.to("kilometer/hour")
```




36.0 kilometer/hour




```python

```


---
**Score: 15**