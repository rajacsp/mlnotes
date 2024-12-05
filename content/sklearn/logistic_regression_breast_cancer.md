---
title: Logistic Regression Breast Cancer
date: 2024-12-05
author: Your Name
cell_count: 4
score: 0
---

---
title: "Logistic Regression Breast Cancer"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
import statsmodels.api as sm
import scipy.stats as st
from statsmodels.tools import add_constant as add_constant
```


```python
df = load_breast_cancer()
df_cancer = pd.DataFrame(np.c_[df['data'], df['target']], columns = np.append(df['feature_names'], ['target']))

df_constant = add_constant(df_cancer)
print(df_constant.head())

st.chisqprob = lambda chisq, df_cancer: st.chi2.sf(chisq, df_cancer)
cols=df_constant.columns[:-1]

model=sm.Logit(df_cancer['target'],df_constant[cols])
result = model.fit(method='bfgs')
print(result.summary())
```

       const  mean radius  mean texture  mean perimeter  mean area  \
    0    1.0        17.99         10.38          122.80     1001.0   
    1    1.0        20.57         17.77          132.90     1326.0   
    2    1.0        19.69         21.25          130.00     1203.0   
    3    1.0        11.42         20.38           77.58      386.1   
    4    1.0        20.29         14.34          135.10     1297.0   
    
       mean smoothness  mean compactness  mean concavity  mean concave points  \
    0          0.11840           0.27760          0.3001              0.14710   
    1          0.08474           0.07864          0.0869              0.07017   
    2          0.10960           0.15990          0.1974              0.12790   
    3          0.14250           0.28390          0.2414              0.10520   
    4          0.10030           0.13280          0.1980              0.10430   
    
       mean symmetry  ...  worst texture  worst perimeter  worst area  \
    0         0.2419  ...          17.33           184.60      2019.0   
    1         0.1812  ...          23.41           158.80      1956.0   
    2         0.2069  ...          25.53           152.50      1709.0   
    3         0.2597  ...          26.50            98.87       567.7   
    4         0.1809  ...          16.67           152.20      1575.0   
    
       worst smoothness  worst compactness  worst concavity  worst concave points  \
    0            0.1622             0.6656           0.7119                0.2654   
    1            0.1238             0.1866           0.2416                0.1860   
    2            0.1444             0.4245           0.4504                0.2430   
    3            0.2098             0.8663           0.6869                0.2575   
    4            0.1374             0.2050           0.4000                0.1625   
    
       worst symmetry  worst fractal dimension  target  
    0          0.4601                  0.11890     0.0  
    1          0.2750                  0.08902     0.0  
    2          0.3613                  0.08758     0.0  
    3          0.6638                  0.17300     0.0  
    4          0.2364                  0.07678     0.0  
    
    [5 rows x 32 columns]
    Warning: Maximum number of iterations has been exceeded.
             Current function value: 0.086366
             Iterations: 35
             Function evaluations: 49
             Gradient evaluations: 41
                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:                 target   No. Observations:                  569
    Model:                          Logit   Df Residuals:                      538
    Method:                           MLE   Df Model:                           30
    Date:                Thu, 16 May 2019   Pseudo R-squ.:                  0.8692
    Time:                        20:13:29   Log-Likelihood:                -49.143
    converged:                      False   LL-Null:                       -375.72
                                            LLR p-value:                2.777e-118
    ===========================================================================================
                                  coef    std err          z      P>|z|      [0.025      0.975]
    -------------------------------------------------------------------------------------------
    const                       0.7822     19.170      0.041      0.967     -36.791      38.356
    mean radius                 3.4536      8.333      0.414      0.679     -12.880      19.787
    mean texture                0.1003      0.227      0.442      0.659      -0.345       0.546
    mean perimeter             -0.4544      1.066     -0.426      0.670      -2.543       1.635
    mean area                   0.0131      0.035      0.377      0.706      -0.055       0.081
    mean smoothness            -0.1647     69.674     -0.002      0.998    -136.722     136.393
    mean compactness           -0.6422     50.294     -0.013      0.990     -99.217      97.932
    mean concavity             -0.9521     33.411     -0.028      0.977     -66.437      64.532
    mean concave points        -0.4439     64.837     -0.007      0.995    -127.523     126.635
    mean symmetry              -0.2247     23.510     -0.010      0.992     -46.303      45.854
    mean fractal dimension     -0.0289    197.700     -0.000      1.000    -387.514     387.456
    radius error               -0.0229     21.225     -0.001      0.999     -41.624      41.578
    texture error               1.7379      1.575      1.103      0.270      -1.349       4.825
    perimeter error             0.2989      1.501      0.199      0.842      -2.642       3.240
    area error                 -0.1326      0.211     -0.628      0.530      -0.547       0.282
    smoothness error           -0.0160    233.330  -6.88e-05      1.000    -457.334     457.302
    compactness error          -0.0872     79.868     -0.001      0.999    -156.626     156.452
    concavity error            -0.1531     42.971     -0.004      0.997     -84.375      84.069
    concave points error       -0.0537    264.665     -0.000      1.000    -518.788     518.681
    symmetry error             -0.0469     85.171     -0.001      1.000    -166.980     166.886
    fractal dimension error    -0.0059    352.904  -1.68e-05      1.000    -691.686     691.674
    worst radius                2.4925      2.723      0.915      0.360      -2.844       7.829
    worst texture              -0.4123      0.219     -1.880      0.060      -0.842       0.017
    worst perimeter            -0.0974      0.233     -0.418      0.676      -0.554       0.359
    worst area                 -0.0413      0.028     -1.499      0.134      -0.095       0.013
    worst smoothness           -0.2963     43.974     -0.007      0.995     -86.484      85.892
    worst compactness          -1.8572     12.273     -0.151      0.880     -25.911      22.197
    worst concavity            -2.4611      8.996     -0.274      0.784     -20.093      15.171
    worst concave points       -0.8269     30.722     -0.027      0.979     -61.041      59.387
    worst symmetry             -0.7000     13.379     -0.052      0.958     -26.922      25.522
    worst fractal dimension    -0.1754     72.544     -0.002      0.998    -142.359     142.008
    ===========================================================================================
    
    Possibly complete quasi-separation: A fraction 0.27 of observations can be
    perfectly predicted. This might indicate that there is complete
    quasi-separation. In this case some parameters will not be identified.


    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/numpy/core/fromnumeric.py:2389: FutureWarning: Method .ptp is deprecated and will be removed in a future version. Use numpy.ptp instead.
      return ptp(axis=axis, out=out, **kwargs)
    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/statsmodels/discrete/discrete_model.py:1724: RuntimeWarning: divide by zero encountered in log
      return np.sum(np.log(self.cdf(q*np.dot(X,params))))
    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/statsmodels/discrete/discrete_model.py:1724: RuntimeWarning: divide by zero encountered in log
      return np.sum(np.log(self.cdf(q*np.dot(X,params))))
    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/statsmodels/base/model.py:508: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
      "Check mle_retvals", ConvergenceWarning)



```python

```


---
**Score: 0**