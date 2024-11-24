---
title: Word-Counter
date: 2024-11-24
author: Your Name
cell_count: 5
score: 5
---

Nov 20 2024

Count Words in a Sentence
Write a program that:

Takes a sentence as input.
Counts the number of words in the sentence.
Prints the count.


```python
def count_words(sentence):
    word_list = sentence.split(" ")

    return len(word_list)
```


```python
count_words("88/99 Redwood Boulevard")
```




    3




```python
count_words("45-67 Maple")
```




    2




```python

```


---
**Score: 5**