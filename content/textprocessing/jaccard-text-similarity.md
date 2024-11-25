---
title: Jaccard-Text-Similarity
date: 2024-11-25
author: Your Name
cell_count: 4
score: 0
---

---
title: "Jaccard Text Similarity"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))
```


```python
content1 = "AI is our friend and it has been friendly"
content2 = "AI and humans have always been friendly"

sim = get_jaccard_sim(content1, content2)

print(sim)
```

    0.3333333333333333



```python

```


---
**Score: 0**