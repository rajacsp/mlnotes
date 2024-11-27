---
title: Get-Specific-Contents
date: 2024-11-27
author: Your Name
cell_count: 6
score: 5
---

---
title: "Get Specific Contents"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
content = """<!DOCTYPE html>

  <!-- The following setting enables collapsible lists -->
  <p>
  <a href="#human">Human</a></p>

  <p class="collapse-section">
  <a class="collapsed collapse-toggle" data-toggle="collapse" 
  href=#mammals>Mammals</a>
  <div class="collapse" id="mammals">
  <ul>
  <li><a href="#alpaca">Alpaca</a>
  <li><a href="#armadillo">Armadillo</a>
  <li><a href="#sequence_only">Armadillo</a> (sequence only)
  <li><a href="#baboon">Baboon</a>
  <li><a href="#bison">Bison</a>
  <li><a href="#bonobo">Bonobo</a>
  <li><a href="#brown_kiwi">Brown kiwi</a>
  <li><a href="#bushbaby">Bushbaby</a>
  <li><a href="#sequence_only">Bushbaby</a> (sequence only)
  <li><a href="#cat">Cat</a>
  <li><a href="#chimp">Chimpanzee</a>
  <li><a href="#chinese_hamster">Chinese hamster</a>
  <li><a href="#chinese_pangolin">Chinese pangolin</a>
  <li><a href="#cow">Cow</a>
  <li><a href="#crab-eating_macaque">Crab-eating_macaque</a>
  <div class="gbFooterCopyright">
  &copy; 2017 The Regents of the University of California. All 
  Rights Reserved.
  <br>
  <a href="https://genome.ucsc.edu/conditions.html">Conditions of 
  Use</a>
  </div>"""
```


```python
content
```




    '<!DOCTYPE html>\n\n  <!-- The following setting enables collapsible lists -->\n  <p>\n  <a href="#human">Human</a></p>\n\n  <p class="collapse-section">\n  <a class="collapsed collapse-toggle" data-toggle="collapse" \n  href=#mammals>Mammals</a>\n  <div class="collapse" id="mammals">\n  <ul>\n  <li><a href="#alpaca">Alpaca</a>\n  <li><a href="#armadillo">Armadillo</a>\n  <li><a href="#sequence_only">Armadillo</a> (sequence only)\n  <li><a href="#baboon">Baboon</a>\n  <li><a href="#bison">Bison</a>\n  <li><a href="#bonobo">Bonobo</a>\n  <li><a href="#brown_kiwi">Brown kiwi</a>\n  <li><a href="#bushbaby">Bushbaby</a>\n  <li><a href="#sequence_only">Bushbaby</a> (sequence only)\n  <li><a href="#cat">Cat</a>\n  <li><a href="#chimp">Chimpanzee</a>\n  <li><a href="#chinese_hamster">Chinese hamster</a>\n  <li><a href="#chinese_pangolin">Chinese pangolin</a>\n  <li><a href="#cow">Cow</a>\n  <li><a href="#crab-eating_macaque">Crab-eating_macaque</a>\n  <div class="gbFooterCopyright">\n  &copy; 2017 The Regents of the University of California. All \n  Rights Reserved.\n  <br>\n  <a href="https://genome.ucsc.edu/conditions.html">Conditions of \n  Use</a>\n  </div>'




```python
import re

regex = r"<li.+?#[^s].+?>(.+)?<\/.+>"

find_matches = re.findall(regex, content)
for matches in find_matches:
    print(matches)
```

    Alpaca
    Armadillo
    Baboon
    Bison
    Bonobo
    Brown kiwi
    Bushbaby
    Cat
    Chimpanzee
    Chinese hamster
    Chinese pangolin
    Cow
    Crab-eating_macaque


Source:
    
    https://stackoverflow.com/questions/56223492/regex-for-extracting-specific-textcontent-in-html-tags


```python

```


---
**Score: 5**