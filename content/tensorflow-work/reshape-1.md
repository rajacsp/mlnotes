---
title: Reshape-1
date: 2024-11-24
author: Your Name
cell_count: 8
score: 5
---

---
title: "Reshape Extra"
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
a = tf.constant([1, 2, 3, 4, 5, 6, 7, 9])
```


```python
b = tf.reshape(a, [2, 4])
```


```python
a
```




    <tf.Tensor 'Const_1:0' shape=(8,) dtype=int32>




```python
b
```




    <tf.Tensor 'Reshape_2:0' shape=(2, 4) dtype=int32>




```python
with tf.Session() as sess:
    b_val = sess.run(b)
    print(b_val)
```

    [[1 2 3 4]
     [5 6 7 9]]



```python

```


---
**Score: 5**