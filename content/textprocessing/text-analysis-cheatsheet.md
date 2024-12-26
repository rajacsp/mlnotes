---
title: Text-Analysis-Cheatsheet
date: 2024-12-26
author: Your Name
cell_count: 5
score: 5
---

---
title: "Template"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---
Basics

#####  tokens

 text1[0:100] - first 101 tokens 
 
 text2[5] - fifth token
 

##### concordance

text3.concordance(‘begat’) - basic keyword-in-context

text1.concordance(‘sea’, lines=100) - show other than default 25 lines

text1.concordance(‘sea’, lines=all) - show all results

text1.concordance(‘sea’, 10, lines=all) - change left and right context width to 10 characters and show all result

moreL http://sapir.psych.wisc.edu/programming_for_psychologists/cheat_sheets/Text-Analysis-with-NLTK-Cheatsheet.pdfmore: 


```python

```


---
**Score: 5**