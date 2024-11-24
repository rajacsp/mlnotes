---
title: Github-Language-Finder
date: 2024-11-24
author: Your Name
cell_count: 4
score: 0
---

---
title: "GitHub Language Finder"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import requests
from bs4 import BeautifulSoup
```


```python
# Collect and parse first page
page = requests.get('https://github.com/getify/BikechainJS')
soup = BeautifulSoup(page.text, 'html.parser')    

#print(soup)

summary_element = soup.select("div.overall-summary")

#print(summary_element)

commits = summary_element[0].select("li.commits span.num")[0].text
commits = str(commits).strip()
print("commits : ", commits)

repo_lang = summary_element[0].select("div.repository-lang-stats li a")

for rl in repo_lang:
    lang = rl.select("span")[1].text
    lang = str(lang).strip()        

    lang_perc = rl.select("span")[2].text
    lang_perc = str(lang_perc).strip()

    print(lang, lang_perc)
```

    commits :  25
    C++ 60.3%
    JavaScript 35.0%
    C 4.7%



```python

```


---
**Score: 0**