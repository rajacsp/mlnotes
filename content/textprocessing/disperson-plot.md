---
title: Disperson-Plot
date: 2024-12-25
author: Your Name
cell_count: 10
score: 10
---

---
title: "Disperson Plot"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.book import text3
```


```python
text3
```




    <Text: The Book of Genesis>




```python
type(text3)
```




    nltk.text.Text




```python
len(text3)
```




    44764




```python
content = ''
counter = 10
for token in text3.tokens:
    counter += 1
    content += token + ' '
    
    if(counter > 200):
        break
    
content
```




    'In the beginning God created the heaven and the earth . And the earth was without form , and void ; and darkness was upon the face of the deep . And the Spirit of God moved upon the face of the waters . And God said , Let there be light : and there was light . And God saw the light , that it was good : and God divided the light from the darkness . And God called the light Day , and the darkness he called Night . And the evening and the morning were the first day . And God said , Let there be a firmament in the midst of the waters , and let it divide the waters from the waters . And God made the firmament , and divided the waters which were under the firmament from the waters which were above the firmame and it was so . And God called the firmament Heaven . And the evening and the morning were the second day . And God said , Let the waters under the heaven be gathered together unto one place '




```python
text3.dispersion_plot(["God", "heaven", "form", "light", "day", ""])
```


    
![png](/mlnotes/images/disperson-plot_6_0.png)
    



```python
text3.dispersion_plot(["citizens", "democracy"])
```


    
![png](/mlnotes/images/disperson-plot_7_0.png)
    



```python

```


```python

```


---
**Score: 10**