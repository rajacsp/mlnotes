---
title: Add-Method
date: 2025-01-04
author: Your Name
cell_count: 16
score: 15
---

---
title: "Add Method"
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
a = tf.Variable(0)
```


```python
b = tf.constant(1)
```


```python
c = tf.add(a, b)
```


```python
c
```




    <tf.Tensor 'Add_2:0' shape=() dtype=int32>




```python
# assign the new value to a
update = tf.assign(a, c)
```


```python
a
```




    <tf.Variable 'Variable_4:0' shape=() dtype=int32_ref>




```python
# You can't change the constant by using assign. 
```


```python
# Initialize global variables

init_op = tf.global_variables_initializer()
session = tf.Session()
session.run(init_op)
```


```python
print(session.run(a))
```

    0



```python
session.run(update)
```




    1




```python
session.run(a)
```




    1




```python
for _ in range(4):
    session.run(update)
    print(session.run(a))
```

    2
    3
    4
    5



```python
session.close()
```


```python

```


---
**Score: 15**