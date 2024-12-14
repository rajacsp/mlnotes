---
title: Cumulatiave Distribution Function 1
date: 2024-12-14
author: Your Name
cell_count: 4
score: 0
---

title: "Cumulative Distribution Function"
author: "Raja CSP Raman"
date: 2019-05-06
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import matplotlib.pyplot as plt
```


```python
data = np.loadtxt('random_timestamp.txt')

print(data)

# Choose how many bins you want here
num_bins = 20

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf
plt.plot(bin_edges[1:], cdf)

plt.show()
```

    [1.37969832e+09 1.37969826e+09 1.37969682e+09 1.37969814e+09
     1.37969802e+09 1.37969856e+09 1.37969664e+09 1.37969676e+09
     1.37969940e+09 1.37969976e+09 1.37969850e+09]


    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:9: VisibleDeprecationWarning: Passing `normed=True` on non-uniform bins has always been broken, and computes neither the probability density function nor the probability mass function. The result is only correct if the bins are uniform, when density=True will produce the same result anyway. The argument will be removed in a future version of numpy.
      if __name__ == '__main__':



    
![png](/mlnotes/images/cumulatiave_distribution_function_1_2_2.png)
    



```python

```


---
**Score: 0**