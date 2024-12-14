---
title: Modify String In Place
date: 2024-12-14
author: Your Name
cell_count: 7
score: 5
---

---
title: "Modify String in Place"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import io
```


```python
s = "Toronto is awesome"
```


```python
sio = io.StringIO(s)
print(sio.getvalue())
```

    Toronto is awesome



```python
sio.seek(11)
sio.write("Wonderful")
```




    9




```python
print(sio.getvalue())
```

    Toronto is Wonderful



```python

```


---
**Score: 5**