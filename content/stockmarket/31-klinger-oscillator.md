---
title: 31-Klinger-Oscillator
date: 2025-05-17
author: Your Name
cell_count: 9
score: 5
---

```python
# Created: 20250104
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
print(pyu.ps2("yfinance pandas matplotlib"))
```

    yfinance==0.2.51
    pandas==2.2.3
    matplotlib==3.9.3
    



```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Calculate Klinger Oscillator
def calculate_klinger(data, short_period=34, long_period=55, signal_period=13):
    # Calculate Trend Direction
    typical_price = data[['High', 'Low', 'Close']].sum(axis=1)
    trend = np.where(typical_price > typical_price.shift(1), 1, -1)
    
    # Calculate Volume Force (VF)
    vf = trend * data['Volume'] * (
        (2 * (data['Close'] - data['Low'] - (data['High'] - data['Close'])) / 
         (data['High'] - data['Low']) - 1)
    )
    vf = vf.fillna(0)
    
    # Calculate Short EMA and Long EMA of VF
    short_ema = vf.ewm(span=short_period, adjust=False).mean()
    long_ema = vf.ewm(span=long_period, adjust=False).mean()
    
    # Klinger Oscillator
    data['Klinger Oscillator'] = short_ema - long_ema
    
    # Signal Line
    data['Signal Line'] = data['Klinger Oscillator'].ewm(span=signal_period, adjust=False).mean()
    
    return data

# Apply Klinger Oscillator calculation
data = calculate_klinger(data)

# Step 3: Plot Close Price and Klinger Oscillator
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot Klinger Oscillator
plt.subplot(2, 1, 2)
plt.plot(data['Klinger Oscillator'], label='Klinger Oscillator', color='purple', linewidth=1.5)
plt.plot(data['Signal Line'], label='Signal Line', color='orange', linestyle='--', linewidth=1.5)
plt.axhline(0, color='black', linestyle='--', linewidth=1, label='Zero Line')
plt.title(f'Klinger Oscillator for {symbol}')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed

    Unexpected exception formatting exception. Falling back to standard exception


    
    Traceback (most recent call last):
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/interactiveshell.py", line 3508, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "/tmp/ipykernel_1242957/3777612313.py", line 38, in <module>
        data = calculate_klinger(data)
               ^^^^^^^^^^^^^^^^^^^^^^^
      File "/tmp/ipykernel_1242957/3777612313.py", line 19, in calculate_klinger
        vf = trend * data['Volume'] * (
             ~~~~~~^~~~~~~~~~~~~~~~
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/generic.py", line 2171, in __array_ufunc__
        return arraylike.array_ufunc(self, ufunc, method, *inputs, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/arraylike.py", line 276, in array_ufunc
        result = maybe_dispatch_ufunc_to_dunder_op(self, ufunc, method, *inputs, **kwargs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "ops_dispatch.pyx", line 113, in pandas._libs.ops_dispatch.maybe_dispatch_ufunc_to_dunder_op
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/ops/common.py", line 76, in new_method
        return method(self, other)
               ^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/arraylike.py", line 206, in __rmul__
        return self._arith_method(other, roperator.rmul)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py", line 7910, in _arith_method
        self, other = self._align_for_op(other, axis, flex=True, level=None)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py", line 8141, in _align_for_op
        right = to_series(right)
                ^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py", line 8133, in to_series
        raise ValueError(
    ValueError: Unable to coerce to Series, length must be 1: given 1006
    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/interactiveshell.py", line 2105, in showtraceback
        stb = self.InteractiveTB.structured_traceback(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/ultratb.py", line 1396, in structured_traceback
        return FormattedTB.structured_traceback(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/ultratb.py", line 1287, in structured_traceback
        return VerboseTB.structured_traceback(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/ultratb.py", line 1140, in structured_traceback
        formatted_exception = self.format_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/ultratb.py", line 1030, in format_exception_as_a_whole
        self.get_records(etb, number_of_lines_of_context, tb_offset) if etb else []
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/ultratb.py", line 1122, in get_records
        FrameInfo(
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/IPython/core/ultratb.py", line 766, in __init__
        ix = inspect.getsourcelines(frame)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/inspect.py", line 1267, in getsourcelines
        lines, lnum = findsource(object)
                      ^^^^^^^^^^^^^^^^^^
      File "/home/rajaraman/miniconda3/envs/ml312-2024/lib/python3.12/inspect.py", line 1088, in findsource
        raise OSError('source code not available')
    OSError: source code not available



```python

```


```python
def show_graph(symbol):

pass
```


```python
show_graph("AMZN")
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[5], line 1
    ----> 1 show_graph("AMZN")


    NameError: name 'show_graph' is not defined



```python

```


---
**Score: 5**