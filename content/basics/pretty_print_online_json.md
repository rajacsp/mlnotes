---
title: Pretty Print Online Json
date: 2024-12-04
author: Your Name
cell_count: 4
score: 0
---

---
title: "Pretty Print Online JSON"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import pprint
import json 
from urllib.request import urlopen
```


```python
r = urlopen("https://mdn.github.io/fetch-examples/fetch-json/products.json")
text = r.read() 
```


```python
pprint.pprint(json.loads(text))
```

    {'products': [{'Location': 'Refrigerated foods',
                   'Name': 'Cheese',
                   'Price': 2.5},
                  {'Location': 'the Snack isle', 'Name': 'Crisps', 'Price': 3},
                  {'Location': 'Refrigerated foods', 'Name': 'Pizza', 'Price': 4},
                  {'Location': 'the Snack isle', 'Name': 'Chocolate', 'Price': 1.5},
                  {'Location': 'Home baking',
                   'Name': 'Self-raising flour',
                   'Price': 1.5},
                  {'Location': 'Home baking',
                   'Name': 'Ground almonds',
                   'Price': 3}]}



---
**Score: 0**