---
title: Simple-Translator-With-Llm
date: 2025-01-04
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
print(pyu.ps2("transformers"))
```

    transformers==4.47.0
    



```python

```


```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
```


```python
model_name = "Helsinki-NLP/opus-mt-en-fi"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
```

    2024-12-22 20:23:01.709850: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
    2024-12-22 20:23:01.721152: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
    WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
    E0000 00:00:1734879181.735845 2038709 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
    E0000 00:00:1734879181.740370 2038709 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
    2024-12-22 20:23:01.755310: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
    To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.



```python
english_text = "Hello, how are you?"
```


```python
# Tokenize the input
inputs = tokenizer.encode(
    english_text, 
    return_tensors = "pt", 
    truncation     = True
)
```


```python
# Generate translation
outputs = model.generate(
    inputs, 
    max_length = 40, 
    num_beams  = 4, 
    early_stopping = True
)
finnish_translation = tokenizer.decode(
    outputs[0], 
    skip_special_tokens = True
)
```


```python
# Print the result
print(f"Original: {english_text}")
print(f"Translated: {finnish_translation}")
```

    Original: Hello, how are you?
    Translated: Hei, mitä kuuluu?



```python

```


---
**Score: 10**