---
title: Phone-Number-Search
date: 2024-12-26
author: Your Name
cell_count: 5
score: 5
---

---
title: "Phone Number Search"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import re
```


```python
fh = open("sample_phone_book.txt")

for line in fh:
    if re.search(r"J.*Neu",line):
        print(line.rstrip())
        
    if re.search(r"a*Neu",line):
        print(line.rstrip())
fh.close()
```

    Allison Neu 555-8396
    Cathy Neu 555-2362
    Jack Neu 555-7666
    Jack Neu 555-7666
    Jeb Neu 555-5543
    Jeb Neu 555-5543
    Jennifer Neu 555-3652
    Jennifer Neu 555-3652
    Ken Neu 555-8752


##### Regex Tips

The special sequences consist of "\\" and a character from the following list:

\d	Matches any decimal digit; equivalent to the set [0-9].

\D	The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].

\s	Matches any whitespace character; equivalent to [ \t\n\r\f\v].

\S	The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].

\w	Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.

\W	Matches the complement of \w.

\b	Matches the empty string, but only at the start or end of a word.

\B	Matches the empty string, but not at the start or end of a word.

\\	Matches a literal backslash.


```python

```


---
**Score: 5**