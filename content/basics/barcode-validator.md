---
title: Barcode-Validator
date: 2024-12-03
author: Your Name
cell_count: 8
score: 5
---

```python

```


```python
# !pip install colormap
```


```python
from PIL import Image
from colormap import rgb2hex
from os import listdir
from os.path import isfile, join, isdir
import os.path as path
```


```python
NON_BARCODE_PAR = 500

def is_barcode_image(filename):
    
    im = Image.open(filename, 'r')
    #width, height = im.size
    pixel_values = list(im.getdata())

    #print(pixel_values)

    color_set = set()

    for p in pixel_values:
        #print(p)
        #print(type(p))

        if(isinstance(p, int)):
            continue

        #return
        if(len(p) > 2):
            h = rgb2hex(p[0], p[1], p[2])

            #print(p, h)
            color_set.add(h)

    #print(color_set)

    colors_length = len(color_set)

    print('colors count : ', colors_length)

    if(colors_length > NON_BARCODE_PAR):
        return 0

    return 1
```


```python
def test_single_image(filename):

    b_result = is_barcode_image(filename)

    if(b_result == 0):
        print('Not a barcode image')
    else:
        print('Barcode image')
```


```python
test_single_image('barcode.jpg')
```

    colors count :  0
    Barcode image



```python
test_single_image('nobar.png')
```

    colors count :  53628
    Not a barcode image



```python

```


---
**Score: 5**