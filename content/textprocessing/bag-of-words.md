---
title: Bag-Of-Words
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

---
title: "Bag of Words"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import re
from nltk.tokenize import word_tokenize
from collections import Counter
```


```python
word_counter = Counter(word_tokenize("""The cat is in the box. The cat likes the box. The box is over the cat."""))
```


```python
print(word_counter)
```

    Counter({'The': 3, 'cat': 3, 'the': 3, 'box': 3, '.': 3, 'is': 2, 'in': 1, 'likes': 1, 'over': 1})



```python
print(word_counter.most_common(4))
```

    [('The', 3), ('cat', 3), ('the', 3), ('box', 3)]



```python

```


---
**Score: 5**