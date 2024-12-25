---
title: Argotranslate-1
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
# !pip install argostranslate
```


```python
print(pyu.ps2("argostranslate"))
```

    argostranslate==1.9.6
    



```python

```


```python
import argostranslate.package
import argostranslate.translate

# Download and install the Finnish language package
from_code = "en"
to_code = "fi"
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code,
        available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# Your contents
contents = [
    "Hello, how are you?",
    "I am doing well, thank you.",
    "What is your name?",
    "My name is Sarah.",
    "Where are you from?"
]

# Translate the contents
translated_contents = [
    argostranslate.translate.translate(text, from_code, to_code)
    for text in contents
]

# Print the results
for original, translated in zip(contents, translated_contents):
    print(f"Original: {original}\nTranslated: {translated}\n")
```

    /home/rajaraman/miniconda3/envs/ml311/lib/python3.11/site-packages/torch/cuda/__init__.py:129: UserWarning: CUDA initialization: CUDA unknown error - this may be due to an incorrectly set up environment, e.g. changing env variable CUDA_VISIBLE_DEVICES after program start. Setting the available devices to be zero. (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.)
      return torch._C._cuda_getDeviceCount() > 0
    /home/rajaraman/miniconda3/envs/ml311/lib/python3.11/site-packages/stanza/models/tokenize/trainer.py:85: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
      checkpoint = torch.load(filename, lambda storage, loc: storage)


    Original: Hello, how are you?
    Translated: Hei, mitä kuuluu?
    
    Original: I am doing well, thank you.
    Translated: Pärjään hyvin, kiitos.
    
    Original: What is your name?
    Translated: Mikä sinun nimesi on?
    
    Original: My name is Sarah.
    Translated: Nimeni on Sarah.
    
    Original: Where are you from?
    Translated: Mistä olet kotoisin?
    


    /home/rajaraman/miniconda3/envs/ml311/lib/python3.11/site-packages/stanza/models/tokenize/trainer.py:85: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
      checkpoint = torch.load(filename, lambda storage, loc: storage)



```python

```


---
**Score: 5**