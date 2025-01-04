---
title: Simple-Text-Processing
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

---
title: "Simple Text Processing"
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
from nltk.corpus import stopwords
```


```python
text = ("""The cat is in the box. The cat likes the box. The box is over the cat.""")
```


```python
tokens = [w for w in word_tokenize(text.lower()) if (w.isalpha() and len(w) > 2)  ]
```


```python
print(tokens)
```

    ['the', 'cat', 'the', 'box', 'the', 'cat', 'likes', 'the', 'box', 'the', 'box', 'over', 'the', 'cat']



```python

```


---
**Score: 5**