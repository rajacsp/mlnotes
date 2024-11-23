```python
import tempfile
```


```python
fp = tempfile.TemporaryFile()
```


```python
fp.name
```




    55




```python
fp.write(b'Hey Toronto')
```




    11




```python
fp.seek(0)
```




    0




```python
fp.read()
```




    b'Hey Toronto'




```python
# Close the file

fp.close()
```


```python

```
