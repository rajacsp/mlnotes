---
title: Index Remover
date: 2025-01-03
author: Your Name
cell_count: 7
score: 5
---

```python

```


```python
"""
input sample:
17. random text1
18. random text2

output:
17, random text1
18, random text2
"""
```




    '\ninput sample:\n17. random text1\n18. random text2\n\noutput:\n17, random text1\n18, random text2\n'




```python
input_sample = """
17. random text1
18. random text2
"""

# Process the input sample
output = []
for line in input_sample.strip().split("\n"):
    number, text = line.split(". ", 1)  # Split by the first occurrence of ". "
    output.append(f"{number}, {text}")

# Combine the processed lines
result = "\n".join(output)
print(result)
```

    17, random text1
    18, random text2



```python
def separate_index(line):

    if ""

    number, text = line.split(". ", 1) 

    return number, text
```


```python
separate_index("18. random text2")
```




    ('18', 'random text2')




```python
separate_index("random text2")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[5], line 1
    ----> 1 separate_index("random text2")


    Cell In[3], line 3, in separate_index(line)
          1 def separate_index(line):
    ----> 3     number, text = line.split(". ", 1) 
          5     return number, text


    ValueError: not enough values to unpack (expected 2, got 1)



```python

```


---
**Score: 5**