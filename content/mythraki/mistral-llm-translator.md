---
title: Mistral-Llm-Translator
date: 2025-05-17
author: Your Name
cell_count: 14
score: 10
---

```python
# https://chatgpt.com/share/6767b5fc-cc44-8002-a0f1-68f486d27d9a
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
# !pip install sacremoses
```


```python
print(pyu.ps2("transformers torch sacremoses"))
```

    transformers==4.47.0
    torch==2.5.1
    sacremoses==0.0.53
    



```python

```


```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load a multilingual model (use a Mistral-based model if available)
model_name = "Helsinki-NLP/opus-mt-en-fi"  # Example model for English to Finnish translation
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Translate a single line
english_text = "Hello, how are you?"

# Tokenize the input
inputs = tokenizer.encode(english_text, return_tensors="pt", truncation=True)

# Generate translation
outputs = model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
finnish_translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print the result
print(f"Original: {english_text}")
print(f"Translated: {finnish_translation}")
```

    Original: Hello, how are you?
    Translated: Hei, mitä kuuluu?



```python

```


```python

```


```python

```


```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class CustomTranslatorWithLLM():

    def __init__(self, language_code):
        model_name = f"Helsinki-NLP/opus-mt-en-{language_code}"  # Example model for English to Finnish translation
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate(self, text):

        # Tokenize the input
        inputs = self.tokenizer.encode(text, return_tensors="pt", truncation=True)
        
        # Generate translation
        outputs = self.model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def separate_index(self, line):

        if ". " in line:
            number, text = line.split(". ", 1)  # Split by the first occurrence of ". "
        else:
            number, text = None, line
    
        return number, text
```


```python

```


```python
translator = CustomTranslatorWithLLM("fi")
```

    /home/rajaraman/miniconda3/envs/ml311/lib/python3.11/site-packages/transformers/models/marian/tokenization_marian.py:175: UserWarning: Recommended: pip install sacremoses.
      warnings.warn("Recommended: pip install sacremoses.")



```python
translator.translate("Where can I get a taxi?")
```




    'Mistä saan taksin?'




```python
contents = """
1. Hello, how are you?
2. I am doing well, thank you.
3. What is your name?
4. My name is Sarah.
"""
```


---
**Score: 10**