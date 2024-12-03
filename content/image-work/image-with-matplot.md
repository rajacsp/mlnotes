---
title: Image-With-Matplot
date: 2024-12-04
author: Your Name
cell_count: 5
score: 5
---

```python
!python --version
```

    Python 3.10.5



```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
```


```python
# Path to your PNG file
image_path = 'deer.jpg'
```


```python
# Load and display the image
img = mpimg.imread(image_path)
plt.imshow(img)
plt.axis('off')  # Turn off axis
plt.show()
```


    
![png](/mlnotes/images/image-with-matplot_3_0.png)
    



```python

```


---
**Score: 5**