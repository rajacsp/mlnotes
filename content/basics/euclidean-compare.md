---
title: Euclidean-Compare
date: 2024-12-04
author: Your Name
cell_count: 9
score: 5
---

---
title: "Euclidean Compare"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import matplotlib
import numpy
import perfplot
from scipy.spatial import distance
```


```python
def linalg_norm(data):
    a, b = data
    return numpy.linalg.norm(a-b, axis=1)
```


```python
def sqrt_sum(data):
    a, b = data
    return numpy.sqrt(numpy.sum((a-b)**2, axis=1))
```


```python
def scipy_distance(data):
    a, b = data
    return map(distance.euclidean, a, b)
```


```python
def mpl_dist(data):
    a, b = data
    return map(matplotlib.mlab.dist, a, b)

```


```python
def sqrt_einsum(data):
    a, b = data
    return numpy.einsum('ij,ij->i', a-b, a-b)**0.5
```


```python
perfplot.show(
    setup=lambda n: numpy.random.rand(2, n, 3),
    n_range=[2**k for k in range(15)],
    kernels=[linalg_norm, scipy_distance, mpl_dist, sqrt_sum, sqrt_einsum],
    logx=True,
    logy=True,
    xlabel='len(x), len(y)'
    )
```

      0%|          | 0/15 [00:00<?, ?it/s]
      0%|          | 0/5 [00:00<?, ?it/s][A
     20%|██        | 1/5 [00:00<00:01,  3.63it/s][A



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-9eaa43e66daa> in <module>()
          5     logx=True,
          6     logy=True,
    ----> 7     xlabel='len(x), len(y)'
          8     )


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/perfplot/main.py in show(*args, **kwargs)
        208 
        209 def show(*args, **kwargs):
    --> 210     out = bench(*args, **kwargs)
        211     out.show()
        212     return


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/perfplot/main.py in bench(setup, kernels, n_range, labels, colors, xlabel, title, target_time_per_measurement, logx, logy, automatic_order, equality_check)
        126                 if equality_check:
        127                     assert equality_check(
    --> 128                         reference, kernel(data)
        129                     ), "Equality check failure. ({}, {})".format(labels[0], labels[k])
        130 


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/numpy/core/numeric.py in allclose(a, b, rtol, atol, equal_nan)
       2421 
       2422     """
    -> 2423     res = all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))
       2424     return bool(res)
       2425 


    ~/anaconda3/envs/py36/lib/python3.6/site-packages/numpy/core/numeric.py in isclose(a, b, rtol, atol, equal_nan)
       2520 
       2521     xfin = isfinite(x)
    -> 2522     yfin = isfinite(y)
       2523     if all(xfin) and all(yfin):
       2524         return within_tol(x, y, atol, rtol)


    TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''



```python

```


---
**Score: 5**