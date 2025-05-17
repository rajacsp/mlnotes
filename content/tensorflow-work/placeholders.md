---
title: Placeholders
date: 2025-05-17
author: Your Name
cell_count: 17
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
# Initialize global variables

init_op = tf.global_variables_initializer()
session = tf.Session()
session.run(init_op)
```


```python
a = tf.placeholder(tf.float32)
```


```python
b = a * a
```


```python
# feeding a placeholder with scalar
result = session.run(b, feed_dict={a:4})
```


```python
print(result)
```

    16.0



```python
result1 = session.run(b, {a:8})
```


```python
result1
```




    64.0




```python
# passing one dimensional array to the placeholder
result2 = session.run(b, {a : [1, 6, 2, 5] })
```


```python
print(result2)
```

    [ 1. 36.  4. 25.]



```python
dictionary = {
    a: [
        [1, 4, 3],
        [2, 2, 4],
        [7, 1, 2]
    ]
}
```


```python
print(dictionary)
```

    {<tf.Tensor 'Placeholder:0' shape=<unknown> dtype=float32>: [[1, 4, 3], [2, 2, 4], [7, 1, 2]]}



```python
result3 = session.run(b, feed_dict=dictionary)
```


```python
print(result3)
```

    [[ 1. 16.  9.]
     [ 4.  4. 16.]
     [49.  1.  4.]]



```python
session.close()
```


```python

```


---
**Score: 15**