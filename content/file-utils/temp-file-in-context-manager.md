---
title: Temp-File-In-Context-Manager
date: 2024-12-14
author: Your Name
cell_count: 6
score: 5
---

---
title: "Temp File in Context Manager"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import tempfile
```


```python
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hey Toronto')
    fp.seek(0)
    print(fp.read())
```

    b'Hey Toronto'



```python
fp
```




    <_io.BufferedRandom name=59>




```python
fp.read()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-8-5b707e20d623> in <module>()
    ----> 1 fp.read()
    

    ValueError: read of closed file



```python
# As you can see the error, the file is already closed. So, you can't read anymore
```


---
**Score: 5**