---
title: Remove-Th-From-Date
date: 2024-12-26
author: Your Name
cell_count: 7
score: 5
---

---
title: "Remove th From Date"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from datetime import datetime
import re
```


```python
content = 'Sunday, May 18th, 2019'
```


```python
content
```




    'Sunday, May 18th, 2019'




```python
d = datetime.strptime(re.sub('(\d+)(st|nd|rd|th)', '\g<1>', content), '%A, %B %d, %Y')
```


```python
d
```




    datetime.datetime(2019, 5, 18, 0, 0)




```python

```


---
**Score: 5**