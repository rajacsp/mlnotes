---
title: Wired-Reader
date: 2024-11-24
author: Your Name
cell_count: 5
score: 5
---

---
title: "Wired Reader"
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
page = requests.get('https://www.wired.com/2013/09/nsa-backdoored-and-stole-keys/')
soup = BeautifulSoup(page.text, 'html.parser')
```


```python
artist_name_list = soup.find(class_='article-body-component')

print(artist_name_list.text[:100])
```

    It was only a matter of time before we learned that the NSA has managed to thwart much of the encryp



```python

```


---
**Score: 5**