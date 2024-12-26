---
title: Compress Image
date: 2024-12-26
author: Your Name
cell_count: 4
score: 0
---

---
title: "Compress Image"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from PIL import Image
```


```python
# Open the image
im = Image.open("/Users/rajacsp/datasets/barcode_images/orange.jpg")

im.save("/Users/rajacsp/datasets/barcode_images/orange_3.jpg", format="JPEG", quality=70)
```


```python

```


---
**Score: 0**