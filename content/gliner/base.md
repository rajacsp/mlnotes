---
title: Base
date: 2025-05-17
author: Your Name
cell_count: 9
score: 5
---

```python
!pip show gliner
```

    Name: gliner
    Version: 0.2.13
    Summary: Generalist model for NER (Extract any entity types from texts)
    Home-page: 
    Author: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois
    Author-email: 
    License: Apache-2.0
    Location: /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages
    Requires: huggingface-hub, onnxruntime, sentencepiece, torch, tqdm, transformers
    Required-by: 



```python
# !pip install gliner
```


```python
from gliner import GLiNER
```


```python
# Initialize GLiNER with a pre-trained model
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")
```


    Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]



    .gitattributes:   0%|          | 0.00/1.52k [00:00<?, ?B/s]



    model.safetensors:   0%|          | 0.00/781M [00:00<?, ?B/s]



    pytorch_model.bin:   0%|          | 0.00/781M [00:00<?, ?B/s]



    README.md:   0%|          | 0.00/4.76k [00:00<?, ?B/s]



    gliner_config.json:   0%|          | 0.00/476 [00:00<?, ?B/s]



    tokenizer_config.json:   0%|          | 0.00/52.0 [00:00<?, ?B/s]



    config.json:   0%|          | 0.00/579 [00:00<?, ?B/s]



    spm.model:   0%|          | 0.00/2.46M [00:00<?, ?B/s]


    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/convert_slow_tokenizer.py:562: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
      warnings.warn(



```python
# Sample text for entity prediction
text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards, a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship, and the UEFA Nations League.
"""
```


```python
# Define the entity labels to identify
labels = ["Person", "Award", "Date", "Competitions", "Teams"]
```


```python
# Perform entity prediction
entities = model.predict_entities(text, labels, threshold=0.5)
```

    Asking to truncate to max_length but no maximum length is provided and the model has no predefined maximum length. Default to no truncation.



```python
# Display predicted entities and their labels
for entity in entities:
    print(f"{entity['text']} => {entity['label']}")
```

    Cristiano Ronaldo dos Santos Aveiro => Person
    5 February 1985 => Date
    Portugal national team => Teams
    UEFA Men's Player of the Year Awards => Award
    European Golden Shoes => Award
    UEFA Champions Leagues => Competitions
    UEFA European Championship => Competitions
    UEFA Nations League => Competitions



```python

```


---
**Score: 5**