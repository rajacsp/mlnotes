---
title: Stack
date: 2024-11-27
author: Your Name
cell_count: 9
score: 5
---

---
author: "Raja CSP Raman"
date: 2019-05-07
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
a = tf.constant([1, 2])
b = tf.constant([3, 4])
c = tf.constant([10, 20])
```


```python
a
```




    <tf.Tensor 'Const_12:0' shape=(2,) dtype=int32>




```python
b
```




    <tf.Tensor 'Const_13:0' shape=(2,) dtype=int32>




```python
d = tf.stack([a, b, c])
```


```python
with tf.Session() as sess:
    d_val = sess.run(d)
    print(a)
    print(d)
    print(d_val)
```

    Tensor("Const_12:0", shape=(2,), dtype=int32)
    Tensor("stack_2:0", shape=(3, 2), dtype=int32)
    [[ 1  2]
     [ 3  4]
     [10 20]]



```python
e = tf.stack([a, b, c], axis=1)

with tf.Session() as sess:
    e_val = sess.run(e)
    print(a)
    print(e)
    print(e_val)
```

    Tensor("Const_12:0", shape=(2,), dtype=int32)
    Tensor("stack_3:0", shape=(2, 3), dtype=int32)
    [[ 1  3 10]
     [ 2  4 20]]



```python

```


---
**Score: 5**