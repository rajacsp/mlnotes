---
title: List-Operations
date: 2024-12-14
author: Your Name
cell_count: 52
score: 50
---

---
title: "List Operations"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
list = [
    "AB", 
    "CD",
    "EF",
    "GH",
    "IJ", 
    "KL",
    "MN",
    "OP",
    "QR",
    "ST",
    "UV",
    "WX",
    "YZ"
]
```


```python
list
```




    ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX', 'YZ']




```python
# append to list
list.append("ABC")
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC']




```python
list.extend(["EFG", "IJK", "LMN"])
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN']




```python
list.extend(("OPQ", "RST"))
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST']




```python
list.extend(range(1, 5))
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4]




```python
list2 = ["One", "Two"]
```


```python
list2
```




    ['One', 'Two']




```python
list.append(list2)
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two']]




```python
list3 = ["Four", "Five"]
```


```python
list += list3
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two'],
     'Four',
     'Five']




```python
list.pop(len(list)-1)
```




    'Five'




```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two'],
     'Four']




```python
list.remove('AB')
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two'],
     'Four']




```python
list.remove(list2)
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four']




```python
list.extend(("ten", "twenty"))
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty']




```python
list.extend(["eleven", "twelve"])
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty',
     'eleven',
     'twelve']




```python
list.append(("six", "seven"))
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty',
     'eleven',
     'twelve',
     ('six', 'seven')]




```python
type(list[len(list)-1])
```




    tuple




```python
del list[len(list)-1]
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty',
     'eleven',
     'twelve']




```python
list.remove("ten")
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
list.append( ["one", "two"])
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve',
     ['one', 'two']]




```python
list.remove(['one', 'two'])
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
# delete elements 1 - 5
del list[1:5]
```


```python
list
```




    ['CD',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
list[::2]
```




    ['CD', 'OP', 'ST', 'WX', 'ABC', 'IJK', 'OPQ', 1, 3, 'Four', 'eleven']




```python
list
```




    ['CD',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
# Remove every 3rd item
del list[::3]
```


```python
list
```




    ['MN',
     'OP',
     'ST',
     'UV',
     'YZ',
     'ABC',
     'IJK',
     'LMN',
     'RST',
     1,
     3,
     4,
     'twenty',
     'eleven']




```python
# Remove every 2nd item
del list[::-3]
```


```python
list
```




    ['MN', 'ST', 'UV', 'ABC', 'IJK', 'RST', 1, 4, 'twenty']




```python
for i, j in enumerate(list):
    print(i, j)
```

    0 MN
    1 ST
    2 UV
    3 ABC
    4 IJK
    5 RST
    6 1
    7 4
    8 twenty



```python
item_index = 1, 4
```


```python
list = [value for key, value in enumerate(list) if key not in item_index]
```


```python
list
```




    ['MN', 'ABC', 'RST', 4, 'twenty']




```python

```


---
**Score: 50**