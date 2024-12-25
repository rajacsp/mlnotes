---
title: Named-Arguments-In-Format
date: 2024-12-25
author: Your Name
cell_count: 4
score: 0
---

---
title: "Named Arguments in Format"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
print("{greeting!r:20}".format(greeting="Hello"))
```

    'Hello'             



```python
print("{one} {two!r}".format(one="ten", two="twenty"))
```

    ten 'twenty'



```python

```


---
**Score: 0**