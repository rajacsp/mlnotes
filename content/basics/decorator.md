---
title: Decorator
date: 2024-12-14
author: Your Name
cell_count: 8
score: 5
---

---
title: "Decorator"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
def rangetest(*argchecks):                  # validate positional arg ranges
    def onDecorator(func):
        def onCall(*args):
            print('argchecks : '+str(argchecks))
            for (ix, low, high) in argchecks:
                print('ix : '+str(ix))
                if args[ix] < low or args[ix] > high:
                    errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                    raise TypeError(errmsg)
            return func(*args)
        return onCall
    return onDecorator
```


```python
class Person:  
    """
    revisit the Person class to validate argument
    """
    def __init__(self, name, job, pay):
        self.job  = job
        self.pay  = pay
                                          # arg 0 is the self instance here
    @rangetest([1, 0.0, 1.0])             # giveRaise = rangetest(..)(giveRaise)
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
```


```python
sue = Person('Sue Jones', 'dev', 100000)
```


```python
sue.pay
```




    100000




```python
sue.giveRaise(0.10)
```

    argchecks : ([1, 0.0, 1.0],)
    ix : 1



```python
sue.pay
```




    110000




```python

```


---
**Score: 5**