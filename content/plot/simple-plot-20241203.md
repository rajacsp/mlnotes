---
title: Simple-Plot-20241203
date: 2025-01-03
author: Your Name
cell_count: 10
score: 10
---

```python

```


```python
!pip show matplotlib | grep "Version:"
```

    Version: 3.9.3



```python
# !pip install matplotlib
```


```python
import matplotlib.pyplot as plt
```


```python
x = [1, 2, 3, 4]
```


```python
y = [50, 40, 80, 40]
```


```python
x, y
```




    ([1, 2, 3, 4], [50, 40, 80, 40])




```python
plt.plot(x, y, 'ro')

plt.axis([0, 10, 20, 100])
```




    (0.0, 10.0, 20.0, 100.0)




    
![png](/mlnotes/images/simple-plot-20241203_7_1.png)
    



```python

```


```python

```


---
**Score: 10**