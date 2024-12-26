---
title: Online Image Reader-2
date: 2024-12-26
author: Your Name
cell_count: 8
score: 5
---

---
title: "Online Image Reader 2"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
import requests
from PIL import Image
from io import BytesIO
```


```python
url = 'https://www.cognex.com/BarcodeGenerator/Content/images/isbn.png'
```


```python
response = requests.get(url)
img = Image.open(BytesIO(response.content))
```


```python
img
```




    
![png](/mlnotes/images/online_image_reader-2_4_0.png)
    




```python
type(img)
```




    PIL.PngImagePlugin.PngImageFile




```python
img.size
```




    (300, 150)




```python

```


---
**Score: 5**