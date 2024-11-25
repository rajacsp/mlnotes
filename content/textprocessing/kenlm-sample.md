---
title: Kenlm-Sample
date: 2024-11-25
author: Your Name
cell_count: 5
score: 5
---

---
title: "Kenlm Sample"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import kenlm
```


```python
model = kenlm.Model('test.arpa')
print(model.score('this is a sentence .', bos = True, eos = True))
```

    -49.579345703125



```python

```


```python

```


---
**Score: 5**