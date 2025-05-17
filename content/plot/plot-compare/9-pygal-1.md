---
title: 9-Pygal-1
date: 2025-05-17
author: Your Name
cell_count: 7
score: 5
---

```python
import pyutil as pyu
```


```python
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python

```


```python
#!pip install pygal
```


```python
!pip show pygal | grep "Version:"
```

    Version: 3.0.5



```python
import pygal

line_chart = pygal.Line()
line_chart.title = "Simple Line Chart"
line_chart.add("Line 1", [1, 3, 5])
line_chart.render_in_browser()
```

    file:///tmp/tmpvx58mc0i.html



```python

```


---
**Score: 5**