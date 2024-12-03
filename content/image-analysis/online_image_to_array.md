---
title: Online Image To Array
date: 2024-12-04
author: Your Name
cell_count: 9
score: 5
---

title: "Online Image to Array"
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




    
![png](/mlnotes/images/online_image_to_array_4_0.png)
    




```python
print(img)
```

    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=500x500 at 0x113092358>



```python
image_array = np.asarray(Image.open('temp.jpg'))
```


```python
image_array.shape
```




    (500, 500, 3)




```python

```


---
**Score: 5**