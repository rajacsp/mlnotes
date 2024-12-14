---
title: Acrony-Finder-Spacy
date: 2024-12-14
author: Your Name
cell_count: 13
score: 10
---

```python

```


```python
# !pip install spacy
```


```python
import spacy
```


```python
spacy.__version__
```




    '3.8.2'




```python
# !python -m spacy download en_core_web_sm
```


```python
import re
```


```python
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")
```


```python
# Sample text
text = "California Xgb is a great tool for machine learning. Another example is AI. \
NTLK is very slow and not recommended high speed ML scenarios. XGBoost, Claude, PrettyMetrics, Rl, Gan, Rnn"
```


```python
# Tokenize and process the text
doc = nlp(text)
```


```python
# Define a function to extract acronyms
def find_acronyms(text):
    # Match patterns for acronyms: Uppercase words or mixed case like "Xgb"
    pattern = re.compile(r'\b[A-Z]{2,5}\b|\b[A-Z][a-zA-Z0-9]{2,4}\b')
    return pattern.findall(text)
```


```python
# Extract acronyms
acronyms = find_acronyms(text)
```


```python
print("Acronyms found:", acronyms)
```

    Acronyms found: ['Xgb', 'AI', 'NTLK', 'ML', 'Gan', 'Rnn']



```python

```


---
**Score: 10**