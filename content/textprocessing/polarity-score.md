---
title: Polarity-Score
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

---
title: "Polarity Score"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer
```


```python
def get_polorize_score(sentence):
    sid = SentimentIntensityAnalyzer()
    
    print(sentence)
    ss = sid.polarity_scores(sentence)
    
    return ss
```


```python
print(get_polorize_score('very Good support for work.'))
```

    very Good support for work.
    {'neg': 0.0, 'neu': 0.327, 'pos': 0.673, 'compound': 0.7328}



```python
print(get_polorize_score('Something went wrong in this model'))
```

    Something went wrong in this model
    {'neg': 0.383, 'neu': 0.617, 'pos': 0.0, 'compound': -0.4767}



```python

```


---
**Score: 5**