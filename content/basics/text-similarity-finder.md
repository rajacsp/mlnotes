---
title: Text-Similarity-Finder
date: 2024-11-27
author: Your Name
cell_count: 5
score: 5
---

---
title: "Text Similarity Finder"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
```


```python
def findSimilarity(param1, param2):
    documents = (
        param1,
        param2
    )
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    cosine = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    
    print(cosine)
```


```python
findSimilarity("In the 1820s Fourier calculated that an object the size of the Earth, and at its distance from the Sun, should be considerably colder than the planet actually is if warmed by only the effects of incoming solar radiation",
                "He examined various possible sources of the additional observed heat in articles published in 1824")
```

    [[1.         0.18965829]]



```python

```


---
**Score: 5**