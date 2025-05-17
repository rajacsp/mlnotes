---
title: Online Image Reader
date: 2025-05-17
author: Your Name
cell_count: 5
score: 5
---

---
title: "Online Image Reader"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
from PIL import Image
import numpy as np
import urllib.request
```


```python
image_path = 'https://multimedia.bbycastatic.ca/multimedia/products/500x500/107/10736/10736343.jpg'
```


```python
with urllib.request.urlopen(image_path) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')
```


```python
img
```




    
![png](/mlnotes/images/online_image_reader_4_0.png)
    




---
**Score: 5**