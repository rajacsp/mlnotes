---
title: Generate-News
date: 2024-11-27
author: Your Name
cell_count: 4
score: 0
---

---
title: "generate news"
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
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')

content_text = """They’re interested in local government, free TV licences, pension credits and child 
trust fund, Carrousel Capital, run by local Liberal Democrats. TV Exclusive Trouser 
Clegg Nick Clegg, but clashed on how the vexing issue of honesty, principles and 
policies of electric shock. It is easy to do. "Louis Vuitton advertising used to pay back 
your debts", he declared that he has delivered his strongest warning yet on the party 
first place and still obsessed with outdated class structures. Inspired by Barack 
Obama’s repertoire, they advise you to send a message to voters at home. "You 
haven’t want to try to counter the threat of it yet," he says. 
"""
tokenized_content = tokenizer.tokenize(content_text)
content_model = nltk.NgramModel(3, tokenized_content)

starting_words = content_model.generate(100)[-2:]
content = content_model.generate(words_to_generate, starting_words)
print(' '.join(content))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-5-a3916bc03d4b> in <module>()
         11 """
         12 tokenized_content = tokenizer.tokenize(content_text)
    ---> 13 content_model = nltk.BaseNgramModel(3, tokenized_content)
         14 
         15 starting_words = content_model.generate(100)[-2:]


    AttributeError: module 'nltk' has no attribute 'BaseNgramModel'



```python

```


---
**Score: 0**