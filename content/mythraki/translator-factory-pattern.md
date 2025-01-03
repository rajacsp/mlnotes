---
title: Translator-Factory-Pattern
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
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    haystack-ai==2.8.0
    ollama-haystack is not installed in the current environment.
    python-dotenv==0.21.0
    



```python

```


```python

```


```python

```


```python

```


```python
from abc import ABC, abstractmethod
from translate import Translator
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from deep_translator import GoogleTranslator
import argostranslate.package
import argostranslate.translate

# Step 1: Define an abstract base class (interface)
class CustomTranslator(ABC):
    @abstractmethod
    def translate(self):
        pass




```


```python
# Step 2: Create concrete implementations of the Shape interface
class CTranslatorVanilla(CustomTranslator):

    def __init__(self, language_code):
        print("vanilla init called")
        self.translator = Translator(to_lang=language_code)
        
    def translate(self, text):
        return self.translator.translate(text)
```


```python
class CTranslatorLLM(CustomTranslator):

    def __init__(self, language_code):
        print("llm init called")
        model_name = f"Helsinki-NLP/opus-mt-en-{language_code}"
        self.translator = Translator(to_lang=language_code)

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
class CTranslatorDeepT(CustomTranslator):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, language_code):

        if not hasattr(self, "initialized"):  # To prevent reinitialization
            print("DeepT init called")
            self.initialized = True
            self.translator = GoogleTranslator(source = 'auto', target = language_code)

    def translate(self, text):
        return self.translator.translate(text)
```


```python
current_language_code = "fi"

# Step 3: Create a Factory class to generate objects
class CustomTranslatorFactory:
    @staticmethod
    def get_custom_translator(translator_type, language_code):
        if translator_type == "vanilla":
            return CTranslatorVanilla(language_code)
        elif translator_type == "llm":
            return CTranslatorLLM(language_code)
        elif translator_type == "deept":
            ctranslator = CTranslatorDeepT(language_code)
        elif translator_type == "argo":
            ctranslator = CTranslatorArgo(language_code)
        else:
            raise ValueError(f"Unknown translator type: {translator_type}")

        return ctranslator
```


```python
class CTranslatorArgo(CustomTranslator):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, language_code):

        if not hasattr(self, "initialized"):  # To prevent reinitialization
            print("Argo init called")
            self.initialized = True
            self.language_code = language_code

            argostranslate.package.update_package_index()
            available_packages = argostranslate.package.get_available_packages()

            package_to_install = next(
                filter(
                    lambda x: x.from_code == "en" and x.to_code == language_code,
                    available_packages
                )
            )
            argostranslate.package.install_from_path(package_to_install.download())

    def translate(self, text):
        return argostranslate.translate.translate(text, "en", self.language_code)
```


```python
# Client Code
if __name__ == "__main__":
    
    # Use the factory to create shapes
    ctranslator_factory = CustomTranslatorFactory()

    current_language_code = "fi"
    
    shape1 = ctranslator_factory.get_custom_translator("deept", current_language_code)
    print(shape1.translate("how are you?"))

    shape2 = ctranslator_factory.get_custom_translator("llm", current_language_code)
    print(shape2.translate("how are you?"))

    shape2 = ctranslator_factory.get_custom_translator("argo", current_language_code)
    print(shape2.translate("where are you?"))
```

    DeepT init called
    kuinka voit?
    llm init called
    Mitä kuuluu?
    Argo init called
    Missä olet?


    /home/rajaraman/miniconda3/envs/ml311/lib/python3.11/site-packages/torch/cuda/__init__.py:129: UserWarning: CUDA initialization: CUDA unknown error - this may be due to an incorrectly set up environment, e.g. changing env variable CUDA_VISIBLE_DEVICES after program start. Setting the available devices to be zero. (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.)
      return torch._C._cuda_getDeviceCount() > 0
    /home/rajaraman/miniconda3/envs/ml311/lib/python3.11/site-packages/stanza/models/tokenize/trainer.py:85: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
      checkpoint = torch.load(filename, lambda storage, loc: storage)



```python

```


```python

```


```python

```


---
**Score: 15**