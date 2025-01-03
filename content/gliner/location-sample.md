---
title: Location-Sample
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

```python

```


```python
from gliner import GLiNER
```


```python
# Initialize GLiNER with a pre-trained model
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")  # Adjust to a location-specific model if needed
```


    Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]


    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/convert_slow_tokenizer.py:562: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
      warnings.warn(



```python
# Input text
text = """
John traveled from New York to San Francisco last week. 
He stopped by Chicago and Denver on his way. His next trip will be to Toronto, Canada.
"""
```


```python
# Define the entity label for location extraction
labels = ["LOCATION"]
```


```python
# Perform entity prediction
locations = model.predict_entities(text, labels, threshold=0.5)
```

    Asking to truncate to max_length but no maximum length is provided and the model has no predefined maximum length. Default to no truncation.



```python
# Display the extracted locations
print("Extracted Locations:")
for loc in locations:
    print(f"{loc['text']} => {loc['label']}")
```

    Extracted Locations:
    New York => LOCATION
    San Francisco => LOCATION
    Chicago => LOCATION
    Denver => LOCATION
    Toronto => LOCATION
    Canada => LOCATION



```python

```


---
**Score: 5**