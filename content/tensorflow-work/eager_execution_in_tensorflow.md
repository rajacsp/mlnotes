---
title: Eager Execution In Tensorflow
date: 2024-11-24
author: Your Name
cell_count: 7
score: 5
---

---
title: "Eager Execution in Tensorflow"
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
tf.enable_eager_execution()
```


```python
a = tf.constant([1.0, 2.0])
```


```python
a
```




    <tf.Tensor: id=3, shape=(2,), dtype=float32, numpy=array([1., 2.], dtype=float32)>




```python
print(a)
```

    tf.Tensor([1. 2.], shape=(2,), dtype=float32)


(Not sure what does it do here. Need to dig more)


---
**Score: 5**