---
title: Variables-With-Type
date: 2024-12-07
author: Your Name
cell_count: 8
score: 5
---

---
title: "Variables with Type"
author: "Raja CSP Raman"
date: 2019-05-06
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
w = tf.Variable([.2], dtype=tf.float32)
```


```python
b = tf.Variable([0.11], dtype=tf.float32)
```


```python
x = tf.placeholder(tf.float32)
```


```python
linear_model = w*x + b
```


```python
linear_model
```




    <tf.Tensor 'add:0' shape=<unknown> dtype=float32>




```python
# Note: variable is used with capital 'V'. However, constants and placeholders start with small case.
```


---
**Score: 5**