---
title: Simple-Session
date: 2025-05-17
author: Your Name
cell_count: 9
score: 5
---

---
title: "Simple Session"
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
hello = tf.constant('Hello, TensorFlow!')
```


```python
hello
```




    <tf.Tensor 'Const:0' shape=() dtype=string>




```python
sess = tf.Session()
sess.run(hello)
```




    b'Hello, TensorFlow!'




```python
a = tf.constant(20)
```


```python
b = tf.constant(30)
```


```python
sess.run(a + b)
```




    50




```python
sess.close()
```


---
**Score: 5**