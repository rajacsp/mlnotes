---
title: Finnish-Translator
date: 2025-01-03
author: Your Name
cell_count: 17
score: 15
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("translate"))
```

    translate==3.6.1
    



```python
# !pip install translate==3.6.1
```


```python
from translate import Translator

# Your contents
contents = [
    "Hello, how are you?",
    "I am doing well, thank you."
]

# Initialize the Translator
translator = Translator(to_lang="fi")  # "fi" is the language code for Finnish

# Translate the contents
translated_contents = [translator.translate(text) for text in contents]

# Print the results
for original, translated in zip(contents, translated_contents):
    print(f"Original: {original}\nTranslated: {translated}\n")
```

    Original: Hello, how are you?
    Translated: Hei, mitä kuuluu?
    
    Original: I am doing well, thank you.
    Translated: Minulla menee hyvin, kiitos.
    



```python
def tranlsate_to(language, text):

    translator = Translator(to_lang="fi")

    translated_content = translator.translate(text)

    return translated_content
```


```python
class CustomTranslator():

    def __init__(self, language):
        self.translator = Translator(to_lang=language)

    def translate(self, text):
        return self.translator.translate(text)

    def separate_index(self, line):

        if ". " in line:
            number, text = line.split(". ", 1)  # Split by the first occurrence of ". "
        else:
            number, text = None, line
    
        return number, text
```


```python
translator = CustomTranslator("fi")
```


```python
translator.translate("hello")
```




    'Hei'




```python
# tranlsate_to("fi")
```


```python
def separate_index(line):

    if ". " in line:
        number, text = line.split(". ", 1)  # Split by the first occurrence of ". "
    else:
        number, text = None, line

    return number, text
```


```python
def read_lines_from_file(file):

    content = None
    with open(file) as f:
        content = f.readlines()

    #print(content)
    #print(type(content))

    return content
```


```python
elines = read_lines_from_file('english.txt')
```


```python
elines
```




    ['91. I am waiting for the bus.\n',
     '92. The train is delayed.\n',
     '93. Where can I get a taxi?\n',
     '94. The traffic is very bad today.\n',
     '95. How long will it take to get there?\n',
     '96. Can you give me directions?\n',
     '97. This is my stop.\n',
     '98. I prefer to walk.\n',
     '99. Is it far from here?\n',
     '100. I need to rent a car.']




```python
translator = CustomTranslator("fi")
```


```python
for line in elines:

    _, cline = translator.separate_index(line)

    translated = translator.translate(cline)

    print(f"{line}")
    print(f"{translated}")
    print("-"*50)
    # print("\n")
```

    91. I am waiting for the bus.
    
    Odotan bussia.
    --------------------------------------------------
    92. The train is delayed.
    
    Juna on myöhässä.
    --------------------------------------------------
    93. Where can I get a taxi?
    
    Mistä voin saada taksin?
    --------------------------------------------------
    94. The traffic is very bad today.
    
    Liikenne on erittäin huonoa tänään.
    --------------------------------------------------
    95. How long will it take to get there?
    
    Kuinka kauan perille pääseminen kestää?
    --------------------------------------------------
    96. Can you give me directions?
    
    Voitko antaa minulle ajo-ohjeet?
    --------------------------------------------------
    97. This is my stop.
    
    Tämä on pysäkkini.
    --------------------------------------------------
    98. I prefer to walk.
    
    Kävelen mieluummin.
    --------------------------------------------------
    99. Is it far from here?
    
    Onko se kaukana täältä?
    --------------------------------------------------
    100. I need to rent a car.
    Minun täytyy vuokrata auto.
    --------------------------------------------------



```python

```


---
**Score: 15**