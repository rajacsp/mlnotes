---
title: "Add Padding Around String"
author: "Raja CSP"
date: 2019-04-20
description: "Add Padding Around String Using Python."
type: technical_note
draft: false
---
## Create Some Text 


```python
text = 'Chapter 2'
```

## Add Padding Around Text 


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


```python

```
