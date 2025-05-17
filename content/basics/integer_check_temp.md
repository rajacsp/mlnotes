---
title: Integer Check Temp
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

---
title: "Integer Check Temp"
author: "Rj"
date: 2019-05-20
description: "Integer Check"
type: technical_note
draft: false
---

```python
content = "23"
```


```python
content
```




    '23'




```python
isinstance(content, int)
```




    False




```python
type(content)
```




    str




```python
content.isdigit()
```




    True




```python
text = "one 2 three 4 five 6 seven 8 nine 10"
```


```python
for x in text.split(" "):
    print(x, "==>", x.isdigit())
```

    one ==> False
    2 ==> True
    three ==> False
    4 ==> True
    five ==> False
    6 ==> True
    seven ==> False
    8 ==> True
    nine ==> False
    10 ==> True



---
**Score: 5**