---
title: Print In Tensorflow
date: 2024-12-26
author: Your Name
cell_count: 8
score: 5
---

---
title: "Print in Tensorflow"
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
a = tf.Variable([[1, 2, 3]])
```


```python
init = (tf.global_variables_initializer(), tf.local_variables_initializer())
```


```python
sess = tf.Session()
```


```python
sess.run(init)
```




    (None, None)




```python
sess.run(a)
```




    array([[1, 2, 3]], dtype=int32)




```python

```


---
**Score: 5**