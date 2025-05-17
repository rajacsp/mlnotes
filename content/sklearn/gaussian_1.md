---
title: Gaussian 1
date: 2025-05-17
author: Your Name
cell_count: 3
score: 0
---

---
title: "Gaussian"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from sklearn.naive_bayes import GaussianNB
import numpy as np
```


```python
#assigning predictor and target variables
x= np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets 
model.fit(x, y)

#Predict Output 
predicted= model.predict([[1,2],[3,4]])
print(predicted)
```

    [3 4]



---
**Score: 0**