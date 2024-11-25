---
title: Word-Cloud-Shutter-Island
date: 2024-11-25
author: Your Name
cell_count: 11
score: 10
---

---
title: "Word Cloud on Shutter Island Script"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS
```


```python
# Read the whole text.
text = open(path.join('', 'script.txt')).read()
```


```python
text[:500]
```




    "DiCarpio\nGet it together Teddy!\nGet it together!\nIt's just water.\nIt's a lot of water\nCome on.\n- You okay boss?\n-Yeah, i'm just...i just can't\nI just can not stand on water.\n- You're my new partner?\n- that's right.\nNot the best way to know you\nhalf head in the toilet.\nDoesn't exactly square with\nTeddy Daniels: the man of legend, i'll give you that\nthe Legend?\nWhat the hell are you boys smoking\nout there in Portland anyway?\nSeatle.\nI came from the office in Seatle.\nHow long have you been with Mar"




```python
# read the mask image
alice_mask = np.array(Image.open(path.join('', "si8.png")))
```


```python
stopwords = set(STOPWORDS)
stopwords.add("said")
```


```python
wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')
```


```python
# generate word cloud
wc.generate(text)
```




    <wordcloud.wordcloud.WordCloud at 0x108649630>




```python
# store to file
wc.to_file(path.join('', "alice.png"))
```




    <wordcloud.wordcloud.WordCloud at 0x108649630>




```python
# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
```


    
![png](/mlnotes/images/word-cloud-shutter-island_9_0.png)
    



    
![png](/mlnotes/images/word-cloud-shutter-island_9_1.png)
    



```python

```


---
**Score: 10**