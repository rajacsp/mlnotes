---
title: Content-Summary
date: 2024-12-14
author: Your Name
cell_count: 6
score: 5
---

---
title: "Content Summary"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from gensim.summarization import summarize, keywords
from pprint import pprint
from smart_open import smart_open
```


```python
text = " ".join((line for line in smart_open('sample.txt', encoding='utf-8')))
```


```python
text
```




    'More than half of survey participants also reported clicking on a headline expecting to read a balanced news account, only to find the story was pushing an agenda.\n \n The survey found 48 per cent of respondents struggled to distinguish between fact and falsehood, while doubts about the authenticity of news stories had jumped 10 per cent in the past year.\n \n The Canadian Journalism Foundation says the survey findings are troubling, particularly in the run-up to a federal election.\n \n The survey, conducted over a five-day period last month, sampled more than 2,300 Canadians.\n \n Online polls cannot be assigned a margin of error, according to the Marketing Research and Intelligence Association.\n'




```python
# Summarize the paragraph
summary = summarize(text, word_count=20)
pprint(summary)
```

    ('More than half of survey participants also reported clicking on a headline '
     'expecting to read a balanced news account, only to find the story was '
     'pushing an agenda.')



```python
print(type(summary))
```

    <class 'str'>



---
**Score: 5**