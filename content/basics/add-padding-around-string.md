---
title: Add-Padding-Around-String
date: 2024-12-25
author: Your Name
cell_count: 9
score: 5
---

```python

```

Create Some Text


```python
text = 'Chapter 2'
```

Add Padding Around Text


```python
# Add Spaces Of Padding To The Left
format(text, '>20')
```




    '           Chapter 2'




```python
# Add Spaces Of Padding To The Right
format(text, '<20')
```




    'Chapter 2           '




```python
# Add Spaces Of Padding On Each Side
format(text, '^20')
```




    '     Chapter 2      '




```python
# Add * Of Padding On Each Side
format(text, '*^20')
```




    '*****Chapter 2******'




```python

```


---
**Score: 5**