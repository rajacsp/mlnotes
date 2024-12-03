---
title: Text-To-Vector
date: 2024-12-03
author: Your Name
cell_count: 9
score: 5
---

---
title: "Text to Vector"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import nltk
```


```python
content = "The Democrats — including more than 50 freshmen — are mindful that impeachment poses political risks that could endanger the seats of moderates and their majority, as well as strengthen Mr. Trump’s hand. "
```


```python
content
```




    'The Democrats — including more than 50 freshmen — are mindful that impeachment poses political risks that could endanger the seats of moderates and their majority, as well as strengthen Mr. Trump’s hand. '




```python
tokens = nltk.word_tokenize(content)
```


```python
tokens
```




    ['The',
     'Democrats',
     '—',
     'including',
     'more',
     'than',
     '50',
     'freshmen',
     '—',
     'are',
     'mindful',
     'that',
     'impeachment',
     'poses',
     'political',
     'risks',
     'that',
     'could',
     'endanger',
     'the',
     'seats',
     'of',
     'moderates',
     'and',
     'their',
     'majority',
     ',',
     'as',
     'well',
     'as',
     'strengthen',
     'Mr.',
     'Trump',
     '’',
     's',
     'hand',
     '.']




```python
type(tokens)
```




    list



##### Why text to vector?

To to machine learning on text, we need to transform our documents into vectors so we can apply numeric machine learning. This is called feature extraction or vectorization.


```python

```


---
**Score: 5**