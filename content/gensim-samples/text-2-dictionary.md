---
title: Text-2-Dictionary
date: 2024-12-07
author: Your Name
cell_count: 10
score: 10
---

---
title: "Text 2 Dictionary"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import gensim
from gensim import corpora
from pprint import pprint
```


```python
# How to create a dictionary from a list of sentences?
documents = [
        """More than half of survey participants also reported clicking on a headline expecting to read a balanced news account, only to find the story was pushing an agenda.
The survey found 48 per cent of respondents struggled to distinguish between fact and falsehood, while doubts about the authenticity of news stories had jumped 10 per cent in the past year.
The Canadian Journalism Foundation says the survey findings are troubling, particularly in the run-up to a federal election."""
    ]
```


```python
documents
```




    ['More than half of survey participants also reported clicking on a headline expecting to read a balanced news account, only to find the story was pushing an agenda.\nThe survey found 48 per cent of respondents struggled to distinguish between fact and falsehood, while doubts about the authenticity of news stories had jumped 10 per cent in the past year.\nThe Canadian Journalism Foundation says the survey findings are troubling, particularly in the run-up to a federal election.']




```python
# Tokenize(split) the sentences into words
tokens = [[text for text in doc.split()] for doc in documents]
```


```python
print(tokens)
```

    [['More', 'than', 'half', 'of', 'survey', 'participants', 'also', 'reported', 'clicking', 'on', 'a', 'headline', 'expecting', 'to', 'read', 'a', 'balanced', 'news', 'account,', 'only', 'to', 'find', 'the', 'story', 'was', 'pushing', 'an', 'agenda.', 'The', 'survey', 'found', '48', 'per', 'cent', 'of', 'respondents', 'struggled', 'to', 'distinguish', 'between', 'fact', 'and', 'falsehood,', 'while', 'doubts', 'about', 'the', 'authenticity', 'of', 'news', 'stories', 'had', 'jumped', '10', 'per', 'cent', 'in', 'the', 'past', 'year.', 'The', 'Canadian', 'Journalism', 'Foundation', 'says', 'the', 'survey', 'findings', 'are', 'troubling,', 'particularly', 'in', 'the', 'run-up', 'to', 'a', 'federal', 'election.']]



```python
# Create dictionary
dictionary = corpora.Dictionary(tokens)
```


```python
dictionary
```




    <gensim.corpora.dictionary.Dictionary at 0x11310f0f0>




```python
print(dictionary)
```

    Dictionary(60 unique tokens: ['10', '48', 'Canadian', 'Foundation', 'Journalism']...)



```python
print(type(dictionary))
```

    <class 'gensim.corpora.dictionary.Dictionary'>



---
**Score: 10**