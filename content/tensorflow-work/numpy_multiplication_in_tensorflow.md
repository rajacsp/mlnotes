---
title: Numpy Multiplication In Tensorflow
date: 2024-11-27
author: Your Name
cell_count: 6
score: 5
---

---
title: "Numpy Multplication in Tensorflow"
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
matrix1 = tf.constant([[3., 3.0]])
matrix2 = tf.constant([[2.0],[2.0]])
product = tf.matmul(matrix1, matrix2)

print(product.numpy()) 
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-3-c077a63dce6d> in <module>()
          3 product = tf.matmul(matrix1, matrix2)
          4 
    ----> 5 print(product.numpy())
    

    AttributeError: 'Tensor' object has no attribute 'numpy'



```python
# The above option is applicable only in Tensorflow 2.0
```


```python
tf.__version__
```




    '1.13.1'




```python

```


---
**Score: 5**