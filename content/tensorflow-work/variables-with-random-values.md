---
title: Variables-With-Random-Values
date: 2024-12-14
author: Your Name
cell_count: 12
score: 10
---

---
title: "Variables With Random Values"
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
a = tf.random_uniform((4, 4), 0, 1)
```


```python
a
```




    <tf.Tensor 'random_uniform_2:0' shape=(4, 4) dtype=float32>




```python
a_var = tf.Variable(initial_value=a)
```


```python
a_var
```




    <tf.Variable 'Variable_2:0' shape=(4, 4) dtype=float32_ref>




```python
sess = tf.Session()
```


```python
init = tf.global_variables_initializer()
```


```python
init
```




    <tf.Operation 'init_2' type=NoOp>




```python
init.run(session=sess)
```


```python
a_var.eval(session=sess)
```




    array([[0.36779773, 0.1853832 , 0.8348143 , 0.6921052 ],
           [0.57980347, 0.49014997, 0.6421398 , 0.91182387],
           [0.510636  , 0.11073005, 0.10901892, 0.11414111],
           [0.7472625 , 0.7295675 , 0.6236193 , 0.5269221 ]], dtype=float32)




```python
sess.run(a_var)
```




    array([[0.36779773, 0.1853832 , 0.8348143 , 0.6921052 ],
           [0.57980347, 0.49014997, 0.6421398 , 0.91182387],
           [0.510636  , 0.11073005, 0.10901892, 0.11414111],
           [0.7472625 , 0.7295675 , 0.6236193 , 0.5269221 ]], dtype=float32)




---
**Score: 10**