---
title: Compress Image Cv2
date: 2024-11-24
author: Your Name
cell_count: 4
score: 0
---

---
title: "Compress Image CV2"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from PIL import Image
import cv2
```


```python
# Open the image
img = cv2.imread('/Users/rajacsp/datasets/barcode_images/orange.jpg')


# save image with lower compression—bigger file size but faster decoding
#cv2.imwrite('/Users/str-kwml0011/datasets/random_images/tv.jpg', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

# check that image saved and loaded again image is the same as original one
#saved_img = cv2.imread(params.out_png)
#assert saved_img.all() == img.all()

# save image with lower quality—smaller file size
cv2.imwrite('/Users/rajacsp/datasets/barcode_images/orange_1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])
```




    True




```python

```


---
**Score: 0**