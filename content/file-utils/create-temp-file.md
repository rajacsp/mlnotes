---
title: Create-Temp-File
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
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




    55




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