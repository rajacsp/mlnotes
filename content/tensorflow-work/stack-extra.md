---
title: Stack-Extra
date: 2024-11-25
author: Your Name
cell_count: 12
score: 10
---

---
title: "Stack Extra"
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
a = tf.constant([
    [1, 2],
    [3, 4]
])
```


```python
a
```




    <tf.Tensor 'Const_4:0' shape=(2, 2) dtype=int32>




```python
b = tf.constant([
    [11, 12],
    [13, 14]
])
```


```python
b
```




    <tf.Tensor 'Const_5:0' shape=(2, 2) dtype=int32>




```python
c = tf.constant([
    [21, 22],
    [23, 24]
])
```


```python
c
```




    <tf.Tensor 'Const_6:0' shape=(2, 2) dtype=int32>




```python
d = tf.stack([a, b, c])
```


```python
d
```




    <tf.Tensor 'stack:0' shape=(3, 2, 2) dtype=int32>




```python
with tf.Session() as sess:
    d_val = sess.run(d)
    print(d_val)
    print(d)
```

    [[[ 1  2]
      [ 3  4]]
    
     [[11 12]
      [13 14]]
    
     [[21 22]
      [23 24]]]
    Tensor("stack:0", shape=(3, 2, 2), dtype=int32)



```python

```


---
**Score: 10**