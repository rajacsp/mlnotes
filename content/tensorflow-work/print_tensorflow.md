---
title: Print Tensorflow
date: 2024-12-03
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
sess = tf.InteractiveSession()
```


```python
sess
```




    <tensorflow.python.client.session.InteractiveSession at 0x12b796668>




```python
a = tf.constant([12.0, 33.0])
```


```python
a
```




    <tf.Tensor 'Const:0' shape=(2,) dtype=float32>




```python
a = tf.Print(a, [a], message='This is a: ')
```

    WARNING:tensorflow:From <ipython-input-6-770d8a3cbb85>:1: Print (from tensorflow.python.ops.logging_ops) is deprecated and will be removed after 2018-08-20.
    Instructions for updating:
    Use tf.print instead of tf.Print. Note that tf.print returns a no-output operator that directly prints the output. Outside of defuns or eager mode, this operator will not be executed unless it is directly specified in session.run or used as a control dependency for other operators. This is only a concern in graph mode. Below is an example of how to ensure tf.print executes in graph mode:
    ```python
        sess = tf.Session()
        with sess.as_default():
            tensor = tf.range(10)
            print_op = tf.print(tensor)
            with tf.control_dependencies([print_op]):
              out = tf.add(tensor, tensor)
            sess.run(out)
        ```
    Additionally, to use tf.print in python 2.7, users must make sure to import
    the following:
    
      `from __future__ import print_function`
    


Note: Print option is removed from Tensorflow


---
**Score: 5**