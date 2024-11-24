---
title: Simple-Tensorflow
date: 2024-11-24
author: Your Name
cell_count: 10
score: 10
---

---
title: "Simple Tensorflow"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```


```python
a = tf.constant(5.0)
```


```python
a
```




    <tf.Tensor 'Const:0' shape=() dtype=float32>




```python
b = tf.constant(3.0)
```


```python
b
```




    <tf.Tensor 'Const_1:0' shape=() dtype=float32>




```python
c = a * b
```


```python
# Lauch session
sess = tf.Session()
```


```python
# Evaluate the tensor c
print(sess.run(c))
```

    15.0



```python

```


---
**Score: 10**