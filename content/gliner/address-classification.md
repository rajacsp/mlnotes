```python
from gliner import GLiNER
```


```python
# Initialize GLiNER with a pre-trained model
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")  # Adjust model as needed
```


    Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]


    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/convert_slow_tokenizer.py:562: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
      warnings.warn(



```python
# Sample text containing a North American address
text = """
1234 Elm Street, Apt 56B, Springfield, IL 62704
5678 Maple Avenue, Suite 101, Denver, CO 80220
9876 Pine Lane, #205, San Francisco, CA 94107
"""
```


```python
# Define the custom labels for entity prediction
labels = ["STREET_NAME", "SUITE_NO", "HOUSE_NO"]
```


```python
# Predict entities in the text
entities = model.predict_entities(text, labels, threshold=0.5)
```

    Asking to truncate to max_length but no maximum length is provided and the model has no predefined maximum length. Default to no truncation.



```python
# Display the predicted entities
print("Extracted Entities:")
for entity in entities:
    print(f"{entity['text']} => {entity['label']}")
```

    Extracted Entities:
    1234 Elm Street => STREET_NAME
    Apt 56B => HOUSE_NO
    5678 => STREET_NAME
    Maple Avenue => STREET_NAME
    Suite 101 => SUITE_NO
    Pine Lane => STREET_NAME
    #205 => SUITE_NO
    94107 => STREET_NAME



```python

```
