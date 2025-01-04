---
title: Text-Decompose
date: 2025-01-04
author: Your Name
cell_count: 4
score: 0
---

---
title: "Text Decompose"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import requests
from bs4 import BeautifulSoup
```


```python
soup = BeautifulSoup('<p>This is a slimy text and <i> I am slimer</i></p>')
soup.i.decompose()
print(soup.text)
```

    This is a slimy text and 



```python

```


---
**Score: 0**