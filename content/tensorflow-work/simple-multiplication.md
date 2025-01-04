---
title: Simple-Multiplication
date: 2025-01-04
author: Your Name
cell_count: 14
score: 10
---

---
title: "Simple Multiplication"
author: "Raja CSP Raman"
date: 2019-05-09
description: "-"
type: technical_note
draft: false
---

```python
import tensorflow as tf

import os

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```


```python
a = tf.random_normal([2, 2])
b = tf.random_normal([2, 2])
```


```python
a
```




    <tf.Tensor 'random_normal_3:0' shape=(2, 2) dtype=float32>




```python
c = tf.matmul(a, b)
```


```python
c
```




    <tf.Tensor 'MatMul_1:0' shape=(2, 2) dtype=float32>




```python
print(c)
```

    Tensor("MatMul_1:0", shape=(2, 2), dtype=float32)



```python
sess = tf.Session()
```


```python
c_val = sess.run(c)
```


```python
c_val
```




    array([[-1.2824252, -0.3110683],
           [-2.3952909,  0.7716379]], dtype=float32)




```python
c_val.shape
```




    (2, 2)




```python
c_val.ndim
```




    2




```python
c.shape.as_list()
```




    [2, 2]




```python

```


---
**Score: 10**