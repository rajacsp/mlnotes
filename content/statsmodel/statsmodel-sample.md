---
title: Statsmodel-Sample
date: 2024-11-27
author: Your Name
cell_count: 8
score: 5
---

---
title: "Stats Model Sample"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import statsmodels.api as sm
```


```python
spector_data = sm.datasets.spector.load()
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/statsmodels/datasets/utils.py:100: FutureWarning: arrays to stack must be passed as a "sequence" type such as list or tuple. Support for non-sequence iterables such as generators is deprecated as of NumPy 1.16 and will raise an error in the future.
      exog = np.column_stack(data[field] for field in exog_name)



```python
spector_data.eog = sm.add_constant(spector_data.exog, prepend=False)
```


```python
# Fit and summarize OLS model

mod = sm.OLS(spector_data.endog, spector_data.exog)
```


```python
res = mod.fit()
```


```python
res
```




    <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x121f11b00>




```python
print(res.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                      y   R-squared:                       0.505
    Model:                            OLS   Adj. R-squared:                  0.454
    Method:                 Least Squares   F-statistic:                     9.852
    Date:                Thu, 25 Apr 2019   Prob (F-statistic):           0.000121
    Time:                        20:23:25   Log-Likelihood:                -17.077
    No. Observations:                  32   AIC:                             40.15
    Df Residuals:                      29   BIC:                             44.55
    Df Model:                           3                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    x1             0.1629      0.137      1.185      0.246      -0.118       0.444
    x2            -0.0136      0.020     -0.692      0.494      -0.054       0.027
    x3             0.3650      0.155      2.349      0.026       0.047       0.683
    ==============================================================================
    Omnibus:                        3.670   Durbin-Watson:                   2.488
    Prob(Omnibus):                  0.160   Jarque-Bera (JB):                2.422
    Skew:                           0.484   Prob(JB):                        0.298
    Kurtosis:                       2.062   Cond. No.                         45.6
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



---
**Score: 5**