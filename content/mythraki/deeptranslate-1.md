---
title: Deeptranslate-1
date: 2024-12-25
author: Your Name
cell_count: 7
score: 5
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
# !pip install deep-translator
```


```python
print(pyu.ps2("deep-translator faker"))
```

    deep-translator==1.11.4
    faker==33.1.0
    



```python

```


```python
from deep_translator import GoogleTranslator

# Your contents
contents = [
    "Hello, how are you?",
    "I am doing well, thank you.",
    "What is your name?",
    "My name is Sarah.",
    "Where are you from?"
]

# Initialize the translator
translator = GoogleTranslator(source='auto', target='fi')  # 'fi' is the language code for Finnish

# Translate the contents
translated_contents = [translator.translate(text) for text in contents]

# Print the results
for original, translated in zip(contents, translated_contents):
    print(f"Original: {original}\nTranslated: {translated}\n")
```

    Original: Hello, how are you?
    Translated: Hei, kuinka voit?
    
    Original: I am doing well, thank you.
    Translated: Voin hyvin, kiitos.
    
    Original: What is your name?
    Translated: Mikä sinun nimesi on?
    
    Original: My name is Sarah.
    Translated: Nimeni on Sarah.
    
    Original: Where are you from?
    Translated: Mistä olet kotoisin?
    



```python

```


---
**Score: 5**