---
title: Append-To-Existing-Dictionary
date: 2024-12-14
author: Your Name
cell_count: 12
score: 10
---

---
title: "Append To Existing Dictionary"
author: "Raja CSP Raman"
date: 2019-05-02
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
# Tokenize(split) the sentences into words
tokens = [[text for text in doc.split()] for doc in documents]
```


```python
# Create dictionary
dictionary = corpora.Dictionary(tokens)
```


```python
print(dictionary)
```

    Dictionary(60 unique tokens: ['10', '48', 'Canadian', 'Foundation', 'Journalism']...)



```python
print(type(dictionary))
```

    <class 'gensim.corpora.dictionary.Dictionary'>



```python
# Show the word to id map
print(dictionary.token2id)
```

    {'10': 0, '48': 1, 'Canadian': 2, 'Foundation': 3, 'Journalism': 4, 'More': 5, 'The': 6, 'a': 7, 'about': 8, 'account,': 9, 'agenda.': 10, 'also': 11, 'an': 12, 'and': 13, 'are': 14, 'authenticity': 15, 'balanced': 16, 'between': 17, 'cent': 18, 'clicking': 19, 'distinguish': 20, 'doubts': 21, 'election.': 22, 'expecting': 23, 'fact': 24, 'falsehood,': 25, 'federal': 26, 'find': 27, 'findings': 28, 'found': 29, 'had': 30, 'half': 31, 'headline': 32, 'in': 33, 'jumped': 34, 'news': 35, 'of': 36, 'on': 37, 'only': 38, 'participants': 39, 'particularly': 40, 'past': 41, 'per': 42, 'pushing': 43, 'read': 44, 'reported': 45, 'respondents': 46, 'run-up': 47, 'says': 48, 'stories': 49, 'story': 50, 'struggled': 51, 'survey': 52, 'than': 53, 'the': 54, 'to': 55, 'troubling,': 56, 'was': 57, 'while': 58, 'year.': 59, '2,300': 60, 'Association.': 61, 'Canadians.': 62, 'Intelligence': 63, 'Marketing': 64, 'Online': 65, 'Research': 66, 'according': 67, 'assigned': 68, 'be': 69, 'cannot': 70, 'conducted': 71, 'error,': 72, 'five-day': 73, 'last': 74, 'margin': 75, 'month,': 76, 'more': 77, 'over': 78, 'period': 79, 'polls': 80, 'sampled': 81, 'survey,': 82}



```python
# Add a new document to the existing dictionary
documents_2 = [
        """The survey, conducted over a five-day period last month, sampled more than 2,300 Canadians.
        Online polls cannot be assigned a margin of error, according to the Marketing Research and Intelligence Association."""
    ]
```


```python
texts_2 = [[text for text in doc.split()] for doc in documents_2]
dictionary.add_documents(texts_2)
```


```python
print(dictionary)
```

    Dictionary(83 unique tokens: ['10', '48', 'Canadian', 'Foundation', 'Journalism']...)



```python
# Show the word to id map
print(dictionary.token2id)
```

    {'10': 0, '48': 1, 'Canadian': 2, 'Foundation': 3, 'Journalism': 4, 'More': 5, 'The': 6, 'a': 7, 'about': 8, 'account,': 9, 'agenda.': 10, 'also': 11, 'an': 12, 'and': 13, 'are': 14, 'authenticity': 15, 'balanced': 16, 'between': 17, 'cent': 18, 'clicking': 19, 'distinguish': 20, 'doubts': 21, 'election.': 22, 'expecting': 23, 'fact': 24, 'falsehood,': 25, 'federal': 26, 'find': 27, 'findings': 28, 'found': 29, 'had': 30, 'half': 31, 'headline': 32, 'in': 33, 'jumped': 34, 'news': 35, 'of': 36, 'on': 37, 'only': 38, 'participants': 39, 'particularly': 40, 'past': 41, 'per': 42, 'pushing': 43, 'read': 44, 'reported': 45, 'respondents': 46, 'run-up': 47, 'says': 48, 'stories': 49, 'story': 50, 'struggled': 51, 'survey': 52, 'than': 53, 'the': 54, 'to': 55, 'troubling,': 56, 'was': 57, 'while': 58, 'year.': 59, '2,300': 60, 'Association.': 61, 'Canadians.': 62, 'Intelligence': 63, 'Marketing': 64, 'Online': 65, 'Research': 66, 'according': 67, 'assigned': 68, 'be': 69, 'cannot': 70, 'conducted': 71, 'error,': 72, 'five-day': 73, 'last': 74, 'margin': 75, 'month,': 76, 'more': 77, 'over': 78, 'period': 79, 'polls': 80, 'sampled': 81, 'survey,': 82}



---
**Score: 10**