---
title: Temp-File
date: 2024-12-06
author: Your Name
cell_count: 9
score: 5
---

---
title: "Create Temp File"
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
fp = tempfile.TemporaryFile()
```


```python
fp.name
```




    57




```python
fp.write(b'Hey Toronto')
```




    11




```python
fp.seek(0)
```




    0




```python
fp.read()
```




    b'Hey Toronto'




```python
# Close the file

fp.close()
```


```python

```


---
**Score: 5**