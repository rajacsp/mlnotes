---
title: Webanalyzer Simple
date: 2025-01-04
author: Your Name
cell_count: 3
score: 0
---

---
title: "Web Analyzer Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import webanalyzer
```


```python
w = webanalyzer.WebAnalyzer()

w.headers = {
    "User-Agent": "custom ua",
    "header-key": "header-value"
}

w.allow_redirect = True
w.aggression = 0
r = w.start("http://www.fatezero.org")

print(r)
```

    [{'name': 'Script', 'origin': 'whatweb'}, {'name': 'HTML5', 'origin': 'whatweb'}, {'name': 'Fastly', 'origin': 'wappalyzer'}, {'name': 'Varnish', 'origin': 'wappalyzer'}, {'name': 'GitHub Pages', 'origin': 'wappalyzer'}, {'name': 'Ruby on Rails', 'origin': 'implies'}, {'name': 'Ruby', 'origin': 'implies'}]



---
**Score: 0**