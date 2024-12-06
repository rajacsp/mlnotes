---
title: Class-2-Json
date: 2024-12-06
author: Your Name
cell_count: 5
score: 5
---

---
title: "Class 2 JSON"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import json
```


```python
class City:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
```


```python
me = City()
me.name = "Onur"
me.id = 1

print(me.toJSON())  
```

    {
        "id": 1,
        "name": "Onur"
    }



```python

```


---
**Score: 5**