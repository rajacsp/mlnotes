---
title: Hybrid-Gliner
date: 2024-11-27
author: Your Name
cell_count: 10
score: 10
---

```python
import re
from gliner import GLiNER
```


```python
# Initialize GLiNER with a pre-trained model
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")  # Replace with a location-specific model if available
```


    Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]


    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/convert_slow_tokenizer.py:562: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
      warnings.warn(



```python
# Input text
text = """
John traveled from New York to San Francisco last week. 
He stopped by Chicago and Denver on his way. His next trip will be to Toronto, Canada. 
He visited the Eiffel Tower in Paris and stayed in London for a week.
"""
```


```python
# Define GLiNER labels
labels = ["LOCATION"]
```


```python
# Step 1: GLiNER's predictions
gliner_predictions = model.predict_entities(text, labels, threshold=0.5)
gliner_locations = {pred['text'] for pred in gliner_predictions}  # Use a set for easy merging
```

    Asking to truncate to max_length but no maximum length is provided and the model has no predefined maximum length. Default to no truncation.



```python
# Step 2: Rules-based predictions using Regex (example for capitalized words indicating locations)
rules_based_predictions = set(re.findall(r"\b[A-Z][a-z]+\b(?: [A-Z][a-z]+)*", text))
```


```python
# Step 3: Combine GLiNER and Rules-Based Predictions
combined_predictions = gliner_locations.union(rules_based_predictions)
```


```python
# Step 4: Optional Heuristic Filtering (e.g., exclude common nouns that aren't locations)
known_non_locations = {"John", "Tower", "week"}
final_predictions = {location for location in combined_predictions if location not in known_non_locations}
```


```python
# Display results
print("GLiNER Predictions:", gliner_locations)
print("Rules-Based Predictions:", rules_based_predictions)
print("Final Combined Predictions:", final_predictions)
```

    GLiNER Predictions: {'Eiffel Tower', 'San Francisco', 'Denver', 'New York', 'Paris', 'Canada', 'Toronto', 'London', 'Chicago'}
    Rules-Based Predictions: {'Eiffel Tower', 'San Francisco', 'Denver', 'His', 'New York', 'John', 'Paris', 'Canada', 'He', 'Toronto', 'London', 'Chicago'}
    Final Combined Predictions: {'Eiffel Tower', 'Denver', 'San Francisco', 'His', 'New York', 'Paris', 'Canada', 'He', 'Toronto', 'London', 'Chicago'}



```python

```


---
**Score: 10**