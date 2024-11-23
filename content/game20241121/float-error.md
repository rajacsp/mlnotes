```python
try:
    "soemthing".toFloat
except (ValueError, KeyError, AttributeError) as e:
    print('error : ', str(e))
    print(getattr(e, 'message', repr(e)))
```

    error :  'str' object has no attribute 'toFloat'
    AttributeError("'str' object has no attribute 'toFloat'")



```python

```
