---
title: Bow-Counts
date: 2024-11-27
author: Your Name
cell_count: 10
score: 10
---

---
title: "Bag of word Counts"
author: "Raja CSP Raman"
date: 2019-05-02
description: "-"
type: technical_note
draft: false
---

```python
from gensim.utils import simple_preprocess
from gensim import corpora
from pprint import pprint
```


```python
contents = [
    "The Star obtained a copy of the email outlining the latest in a series of Progressive Conservative provincial budget cuts that could cost the City of Toronto, over the next decade, billions of dollars in funding for transit, public health and more.",
    "Toronto councillors and daycare advocates are expected to hold a news conference Friday demanding the Ford government reverse the elimination of a $50-million fund that helps licensed child-care centres cover increasing labour costs and shield parents from fee increases, along with other changes."
]
```


```python
contents
```




    ['The Star obtained a copy of the email outlining the latest in a series of Progressive Conservative provincial budget cuts that could cost the City of Toronto, over the next decade, billions of dollars in funding for transit, public health and more.',
     'Toronto councillors and daycare advocates are expected to hold a news conference Friday demanding the Ford government reverse the elimination of a $50-million fund that helps licensed child-care centres cover increasing labour costs and shield parents from fee increases, along with other changes.']




```python
# Get the tokens
tokens = [simple_preprocess(doc) for doc in contents]
```


```python
pprint(tokens)
```

    [['the',
      'star',
      'obtained',
      'copy',
      'of',
      'the',
      'email',
      'outlining',
      'the',
      'latest',
      'in',
      'series',
      'of',
      'progressive',
      'conservative',
      'provincial',
      'budget',
      'cuts',
      'that',
      'could',
      'cost',
      'the',
      'city',
      'of',
      'toronto',
      'over',
      'the',
      'next',
      'decade',
      'billions',
      'of',
      'dollars',
      'in',
      'funding',
      'for',
      'transit',
      'public',
      'health',
      'and',
      'more'],
     ['toronto',
      'councillors',
      'and',
      'daycare',
      'advocates',
      'are',
      'expected',
      'to',
      'hold',
      'news',
      'conference',
      'friday',
      'demanding',
      'the',
      'ford',
      'government',
      'reverse',
      'the',
      'elimination',
      'of',
      'million',
      'fund',
      'that',
      'helps',
      'licensed',
      'child',
      'care',
      'centres',
      'cover',
      'increasing',
      'labour',
      'costs',
      'and',
      'shield',
      'parents',
      'from',
      'fee',
      'increases',
      'along',
      'with',
      'other',
      'changes']]



```python
# Create the dictionary
dict = corpora.Dictionary()
```


```python
# Create the Corpus
corpus1 = [dict.doc2bow(doc, allow_update=True) for doc in tokens]
```


```python
word_counts = [[(dict[id], count) for id, count in line]for line in corpus1]
```


```python
pprint(word_counts)
```

    [[('and', 1),
      ('billions', 1),
      ('budget', 1),
      ('city', 1),
      ('conservative', 1),
      ('copy', 1),
      ('cost', 1),
      ('could', 1),
      ('cuts', 1),
      ('decade', 1),
      ('dollars', 1),
      ('email', 1),
      ('for', 1),
      ('funding', 1),
      ('health', 1),
      ('in', 2),
      ('latest', 1),
      ('more', 1),
      ('next', 1),
      ('obtained', 1),
      ('of', 4),
      ('outlining', 1),
      ('over', 1),
      ('progressive', 1),
      ('provincial', 1),
      ('public', 1),
      ('series', 1),
      ('star', 1),
      ('that', 1),
      ('the', 5),
      ('toronto', 1),
      ('transit', 1)],
     [('and', 2),
      ('of', 1),
      ('that', 1),
      ('the', 2),
      ('toronto', 1),
      ('advocates', 1),
      ('along', 1),
      ('are', 1),
      ('care', 1),
      ('centres', 1),
      ('changes', 1),
      ('child', 1),
      ('conference', 1),
      ('costs', 1),
      ('councillors', 1),
      ('cover', 1),
      ('daycare', 1),
      ('demanding', 1),
      ('elimination', 1),
      ('expected', 1),
      ('fee', 1),
      ('ford', 1),
      ('friday', 1),
      ('from', 1),
      ('fund', 1),
      ('government', 1),
      ('helps', 1),
      ('hold', 1),
      ('increases', 1),
      ('increasing', 1),
      ('labour', 1),
      ('licensed', 1),
      ('million', 1),
      ('news', 1),
      ('other', 1),
      ('parents', 1),
      ('reverse', 1),
      ('shield', 1),
      ('to', 1),
      ('with', 1)]]



---
**Score: 10**