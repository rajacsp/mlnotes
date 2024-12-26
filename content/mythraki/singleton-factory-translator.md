---
title: Singleton-Factory-Translator
date: 2024-12-26
author: Your Name
cell_count: 11
score: 10
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==0.21.0
    



```python

```


```python
from abc import ABC, abstractmethod
from translate import Translator
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Step 1: Define an abstract base class (interface)
class CustomTranslator(ABC):
    @abstractmethod
    def translate(self):
        pass
```


```python
class CTranslatorVanilla(CustomTranslator):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, language_code):

        if not hasattr(self, "initialized"):  # To prevent reinitialization
            print("vanilla init called")
            self.initialized = True
            self.translator = Translator(to_lang=language_code)
        
    def translate(self, text):
        return self.translator.translate(text)
```


```python
class CTranslatorLLM(CustomTranslator):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, language_code):

        if not hasattr(self, "initialized"):  # To prevent reinitialization
            print("llm init called")
            self.initialized = True
            
            model_name = f"Helsinki-NLP/opus-mt-en-{language_code}"
    
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
    def translate(self, text):

        # Tokenize the input
        inputs = self.tokenizer.encode(text, return_tensors="pt", truncation=True)
        
        # Generate translation
        outputs = self.model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
```


```python
current_language_code = "fi"

# Step 3: Create a Factory class to generate objects
class CustomTranslatorFactory:
    @staticmethod
    def get_custom_translator(translator_type):
        if translator_type == "vanilla":
            return CTranslatorVanilla(current_language_code)
        elif translator_type == "llm":
            return CTranslatorLLM(current_language_code)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
```


```python
# Client Code
if __name__ == "__main__":
    # Use the factory to create shapes
    ctranslator_factory = CustomTranslatorFactory()
    
    shape1 = ctranslator_factory.get_custom_translator("vanilla")
    print(shape1.translate("how are you?"))

    shape2 = ctranslator_factory.get_custom_translator("llm")
    print(shape2.translate("how are you?"))

    shape2 = ctranslator_factory.get_custom_translator("llm")
    print(shape2.translate("where are you?"))
```

    Miten voit?
    llm init called
    Mitä kuuluu?
    Missä olet?



```python

```


```python

```


---
**Score: 10**