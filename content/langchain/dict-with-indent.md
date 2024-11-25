---
title: Dict-With-Indent
date: 2024-11-25
author: Your Name
cell_count: 4
score: 0
---

```python
import json

# Example dictionary
result_dict = {
    "name": "John Doe",
    "age": 30,
    "location": {
        "city": "New York",
        "country": "USA"
    }
}

# Convert dictionary to JSON string with indentation
formatted_json = json.dumps(result_dict, indent=4)

# Print the formatted JSON
print(formatted_json)

```

    {
        "name": "John Doe",
        "age": 30,
        "location": {
            "city": "New York",
            "country": "USA"
        }
    }



```python
from IPython.display import JSON
```


```python
JSON(result_dict)
```




    <IPython.core.display.JSON object>




```python

```


---
**Score: 0**