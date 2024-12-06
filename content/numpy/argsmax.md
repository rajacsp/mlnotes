---
title: Argsmax
date: 2024-12-06
author: Your Name
cell_count: 24
score: 20
---

```python
import numpy as np
```


```python
a = np.array(
    [
        [1,2,44,7], 
        [9,88,6,45], 
        [19,76,3,4]
    ]
)
```


```python
a
```




    array([[ 1,  2, 44,  7],
           [ 9, 88,  6, 45],
           [19, 76,  3,  4]])




```python
a.size
```




    12




```python
a.shape
```




    (3, 4)




```python
a.ndim
```




    2




```python
np.argmax(a)
```




    5




```python
a.flatten()
```




    array([ 1,  2, 44,  7,  9, 88,  6, 45, 19, 76,  3,  4])



Note:

argmax Returns the indices of the maximum values along an axis.

The np.argmax function by default works along the flattened array, unless you specify an axis


```python
np.argmin(a) # returns the index of the minimum value
```




    0




```python
np.argmax(a, axis=0) # index of numbers 19, 88, 44, 45
```




    array([2, 1, 0, 1])



Note

np.argmax(a, axis=0) returns the index of the maximum value in each of the four columns.


```python
np.argmax(a, axis=1)
```




    array([2, 1, 1])



Note:

That means np.argmax(a, axis=1) returns
2,1,1
because a has three rows. The index of the maximum value in the first row is 2 (44), the index of the maximum value of the second and third rows is 1 (88, 76)


```python
b = np.array(
    [
        [2, 4], 
        [5, 3] 
       
    ]
)
```


```python
b
```




    array([[2, 4],
           [5, 3]])




```python
b.size
```




    4




```python
b.shape
```




    (2, 2)




```python
b.flatten()
```




    array([2, 4, 5, 3])




```python
np.argmax(b)
```




    2




```python
np.argmax(b, axis=0)
```




    array([1, 0])




```python
np.argmax(b, axis=1)
```




    array([1, 0])



https://stackoverflow.com/questions/28697993/numpy-what-is-the-logic-of-the-argmin-and-argmax-functions


```python

```


---
**Score: 20**