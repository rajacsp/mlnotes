---
title: Frequency-Distribution
date: 2024-11-24
author: Your Name
cell_count: 13
score: 10
---

---
title: "Frequeyncy Distribution"
author: "Rj"
date: 2019-04-29
description: "-"
type: technical_note
draft: false
---

```python
# https://www.azlyrics.com/lyrics/fifthharmony/worthit.html
lyrics = """
Give it to me, I'm worth it
Baby, I'm worth it
Uh huh I'm worth it
Gimme gimme I'm worth it
Give it to me, I'm worth it
Baby, I'm worth it
Uh huh I'm worth it
Gimme gimme I'm worth it

OK, I tell her bring it back like she left some-
Bring it bring it back like she left some-
In the club with the lights off
Whatchu acting shy for?
Come and show me that you're with it with it with it with it with it
Stop playing, now you know that I'm with it with it with it with it with it with it
Whatchu acting shy for?
"""
```


```python
lyrics
```




    "\nGive it to me, I'm worth it\nBaby, I'm worth it\nUh huh I'm worth it\nGimme gimme I'm worth it\nGive it to me, I'm worth it\nBaby, I'm worth it\nUh huh I'm worth it\nGimme gimme I'm worth it\n\nOK, I tell her bring it back like she left some-\nBring it bring it back like she left some-\nIn the club with the lights off\nWhatchu acting shy for?\nCome and show me that you're with it with it with it with it with it\nStop playing, now you know that I'm with it with it with it with it with it with it\nWhatchu acting shy for?\n"




```python
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import nltk
```


```python
tokens = nltk.word_tokenize(lyrics)

#Create your bigrams
bgs = nltk.bigrams(tokens)
```


```python
fdist = FreqDist()
```


```python
fdist = FreqDist(bgs)
```


```python
fdist.plot(30,cumulative=False)
```


    
![png](/mlnotes/images/frequency-distribution_7_0.png)
    



```python
#compute frequency distribution for all the bigrams in the text
for k,v in fdist.items():
    print(k,v)
```


```python
fdist.items()
```




    dict_items([])




```python
from nltk.util import ngrams    

bigramfdist = FreqDist()
threeramfdist = FreqDist()

for line in lyrics:
    if len(line) > 1:
        tokens = line.strip().split(' ')

    bigrams = ngrams(tokens, 2)
    bigramfdist.update(bigrams)
```


```python
bigramfdist.plot()
```


    
![png](/mlnotes/images/frequency-distribution_11_0.png)
    



```python

```


---
**Score: 10**