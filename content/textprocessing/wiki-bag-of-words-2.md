---
title: Wiki-Bag-Of-Words-2
date: 2024-11-24
author: Your Name
cell_count: 7
score: 5
---

---
title: "Wiki Bag of Words 2"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import re
from nltk.tokenize import word_tokenize
from collections import Counter
```


```python
article = """Natural lead consists of four stable isotopes with mass numbers of 204, 206, 207, and 208,[27] and traces of five short-lived radioisotopes.[28] The high number of isotopes is consistent with lead's atomic number being even.[g] Lead has a magic number of protons (82), for which the nuclear shell model accurately predicts an especially stable nucleus. Lead-208 has 126 neutrons, another magic number, which may explain why lead-208 is extraordinarily stable.[29]

With its high atomic number, lead is the heaviest element whose natural isotopes are regarded as stable. This title was formerly held by bismuth, with an atomic number of 83, until its only primordial isotope, bismuth-209, was found in 2003 to decay very slowly.[h] The four stable isotopes of lead could theoretically undergo alpha decay to isotopes of mercury with a release of energy, but this has not been observed for any of them; their predicted half-lives range from 1035 to 10189 years.[32]

Three of the stable isotopes are found in three of the four major decay chains: lead-206, lead-207, and lead-208 are the final decay products of uranium-238, uranium-235, and thorium-232, respectively. These decay chains are called the uranium series, the actinium series, and the thorium series. Their isotopic concentration in a natural rock sample depends greatly on the presence of these three parent uranium and thorium isotopes. For example, the relative abundance of lead-208 can range from 52% in normal samples to 90% in thorium ores;[33] for this reason, the standard atomic weight of lead is given to only one decimal place.[34] As time passes, the ratio of lead-206 and lead-207 to lead-204 increases, since the former two are supplemented by radioactive decay of heavier elements while the latter is not; this allows for lead–lead dating. As uranium decays into lead, their relative amounts change; this is the basis for uranium–lead dating.[35]""";

```


```python
# Tokenize the article: tokens (only more than 5 letters are accepted)
lower_tokens = [t for t in word_tokenize(article.lower()) if (len(t) > 5) ]
```


```python
# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)
```


```python
print(bow_simple.most_common(10))
```

    [('isotopes', 7), ('stable', 6), ('number', 6), ('atomic', 4), ('lead-208', 4), ('natural', 3), ('uranium', 3), ('series', 3), ('thorium', 3), ('chains', 2)]



```python

```


---
**Score: 5**