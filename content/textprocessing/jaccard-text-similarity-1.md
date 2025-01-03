---
title: Jaccard-Text-Similarity-1
date: 2025-01-03
author: Your Name
cell_count: 4
score: 0
---

---
title: "Jaccard Text Similarity 1"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
def get_jaccard_similarity(content1, content2): 
    
    content1_similarity = set(content1.split()) 
    content2_similarity = set(content2.split())
    
    
    intersection = content1_similarity.intersection(content2_similarity)
    
    return float(len(intersection)) / (len(content1_similarity) + len(content2_similarity) - len(intersection))
```


```python
# test 2  
content1 = "These data could show that the people of Brazil are happy with product A, while the people of the US are happier with product B. With NLP, this knowledge can be found instantly (i.e. a real-time result). For example, search engines are a type of NLP that give the appropriate results to the right people at the right time."
# source: https://dzone.com/articles/nlp-tutorial-using-python-nltk-simple-examples    

print(content1.split())

content2 = "These data could show that the people of Brazil are happy with product A, while the people of the US are happier with product B. With NLP, this knowledge can be found instantly (i.e. a real-time result). For example, search engines are a type of NLP that give the appropriate results to the right people at the right time."    
# source : https://www.linkedin.com/pulse/machine-learning-natural-language-processing-sentiment-sharma/

sim = get_jaccard_similarity(content1, content2)    
print(sim)
```

    ['These', 'data', 'could', 'show', 'that', 'the', 'people', 'of', 'Brazil', 'are', 'happy', 'with', 'product', 'A,', 'while', 'the', 'people', 'of', 'the', 'US', 'are', 'happier', 'with', 'product', 'B.', 'With', 'NLP,', 'this', 'knowledge', 'can', 'be', 'found', 'instantly', '(i.e.', 'a', 'real-time', 'result).', 'For', 'example,', 'search', 'engines', 'are', 'a', 'type', 'of', 'NLP', 'that', 'give', 'the', 'appropriate', 'results', 'to', 'the', 'right', 'people', 'at', 'the', 'right', 'time.']
    1.0



```python

```


---
**Score: 0**