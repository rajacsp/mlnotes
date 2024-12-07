---
title: 5-Hyperband-1
date: 2024-12-07
author: Your Name
cell_count: 16
score: 15
---

```python

```


```python
import pyutil as pyu
```


```python
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python

```


```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
import optuna
from optuna.pruners import HyperbandPruner
```


```python
# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = pd.read_csv(url)
```


```python
# Preprocessing
# Select features and target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = data[features]
y = data['Survived']
```


```python
# Handle missing values
X.loc[:, 'Age'] = X['Age'].fillna(X['Age'].median())
X.loc[:, 'Embarked'] = X['Embarked'].fillna(X['Embarked'].mode()[0])
```


```python
# Convert categorical variables to numerical
X = pd.get_dummies(X, columns=['Sex', 'Embarked'], drop_first=True)
```


```python
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```


```python
# Define the objective function for Hyperband optimization
def objective(trial):
    # Define hyperparameters to optimize
    n_estimators = trial.suggest_int('n_estimators', 100, 500)
    max_depth = trial.suggest_int('max_depth', 5, 20)
    min_samples_split = trial.suggest_int('min_samples_split', 2, 10)
    
    # Create the model with suggested hyperparameters
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )
    
    # Perform cross-validation
    score = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy', n_jobs=-1)
    return np.mean(score)
```


```python
# Create the Optuna study with Hyperband pruning
study = optuna.create_study(
    direction='maximize',
    pruner=HyperbandPruner()
)
study.optimize(objective, n_trials=50)
```

    [I 2024-12-06 13:07:27,112] A new study created in memory with name: no-name-1849c918-a1d5-4c67-b311-d9cccb6cb56f
    [I 2024-12-06 13:07:30,699] Trial 0 finished with value: 0.8117994681374963 and parameters: {'n_estimators': 272, 'max_depth': 13, 'min_samples_split': 7}. Best is trial 0 with value: 0.8117994681374963.
    [I 2024-12-06 13:07:33,573] Trial 1 finished with value: 0.8258347286516301 and parameters: {'n_estimators': 259, 'max_depth': 20, 'min_samples_split': 10}. Best is trial 1 with value: 0.8258347286516301.
    [I 2024-12-06 13:07:34,649] Trial 2 finished with value: 0.8286220821432089 and parameters: {'n_estimators': 192, 'max_depth': 12, 'min_samples_split': 9}. Best is trial 2 with value: 0.8286220821432089.
    [I 2024-12-06 13:07:35,514] Trial 3 finished with value: 0.8328277356446371 and parameters: {'n_estimators': 174, 'max_depth': 7, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:36,032] Trial 4 finished with value: 0.8258150300403821 and parameters: {'n_estimators': 118, 'max_depth': 5, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:36,715] Trial 5 finished with value: 0.8118191667487442 and parameters: {'n_estimators': 135, 'max_depth': 16, 'min_samples_split': 4}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:37,622] Trial 6 finished with value: 0.8216290751502019 and parameters: {'n_estimators': 155, 'max_depth': 12, 'min_samples_split': 3}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:39,624] Trial 7 finished with value: 0.8314291342460356 and parameters: {'n_estimators': 351, 'max_depth': 6, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:41,758] Trial 8 finished with value: 0.8257953314291344 and parameters: {'n_estimators': 428, 'max_depth': 6, 'min_samples_split': 4}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:42,722] Trial 9 finished with value: 0.8146163695459471 and parameters: {'n_estimators': 170, 'max_depth': 17, 'min_samples_split': 7}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:44,483] Trial 10 finished with value: 0.8159657244164287 and parameters: {'n_estimators': 344, 'max_depth': 8, 'min_samples_split': 6}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:46,322] Trial 11 finished with value: 0.8187826258248794 and parameters: {'n_estimators': 392, 'max_depth': 9, 'min_samples_split': 8}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:47,879] Trial 12 finished with value: 0.8257953314291342 and parameters: {'n_estimators': 344, 'max_depth': 8, 'min_samples_split': 10}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:50,375] Trial 13 finished with value: 0.8244262779474048 and parameters: {'n_estimators': 495, 'max_depth': 10, 'min_samples_split': 6}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:51,633] Trial 14 finished with value: 0.8244164286417808 and parameters: {'n_estimators': 244, 'max_depth': 5, 'min_samples_split': 8}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:53,200] Trial 15 finished with value: 0.8272037821333595 and parameters: {'n_estimators': 316, 'max_depth': 7, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:54,354] Trial 16 finished with value: 0.8159952723333006 and parameters: {'n_estimators': 231, 'max_depth': 10, 'min_samples_split': 7}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:56,151] Trial 17 finished with value: 0.8160346695557964 and parameters: {'n_estimators': 420, 'max_depth': 14, 'min_samples_split': 5}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:56,602] Trial 18 finished with value: 0.8286319314488327 and parameters: {'n_estimators': 103, 'max_depth': 7, 'min_samples_split': 2}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:57,757] Trial 19 finished with value: 0.8173643258150299 and parameters: {'n_estimators': 307, 'max_depth': 10, 'min_samples_split': 10}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:59,247] Trial 20 finished with value: 0.828612232837585 and parameters: {'n_estimators': 376, 'max_depth': 6, 'min_samples_split': 8}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:07:59,707] Trial 21 finished with value: 0.8300305328474342 and parameters: {'n_estimators': 105, 'max_depth': 7, 'min_samples_split': 2}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:00,567] Trial 22 finished with value: 0.8258150300403821 and parameters: {'n_estimators': 215, 'max_depth': 8, 'min_samples_split': 2}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:01,173] Trial 23 finished with value: 0.8244164286417808 and parameters: {'n_estimators': 175, 'max_depth': 5, 'min_samples_split': 5}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:01,663] Trial 24 finished with value: 0.8314291342460356 and parameters: {'n_estimators': 132, 'max_depth': 7, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:02,659] Trial 25 finished with value: 0.821609376538954 and parameters: {'n_estimators': 281, 'max_depth': 11, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:03,344] Trial 26 finished with value: 0.8173643258150299 and parameters: {'n_estimators': 198, 'max_depth': 9, 'min_samples_split': 8}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:04,488] Trial 27 finished with value: 0.8271939328277357 and parameters: {'n_estimators': 335, 'max_depth': 7, 'min_samples_split': 10}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:06,211] Trial 28 finished with value: 0.8243967300305328 and parameters: {'n_estimators': 457, 'max_depth': 9, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:06,862] Trial 29 finished with value: 0.8104107160445189 and parameters: {'n_estimators': 149, 'max_depth': 14, 'min_samples_split': 7}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:07,908] Trial 30 finished with value: 0.828612232837585 and parameters: {'n_estimators': 288, 'max_depth': 6, 'min_samples_split': 8}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:08,316] Trial 31 finished with value: 0.8272234807446074 and parameters: {'n_estimators': 103, 'max_depth': 7, 'min_samples_split': 6}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:08,779] Trial 32 finished with value: 0.8229882793263075 and parameters: {'n_estimators': 130, 'max_depth': 6, 'min_samples_split': 3}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:09,452] Trial 33 finished with value: 0.8243770314192849 and parameters: {'n_estimators': 188, 'max_depth': 8, 'min_samples_split': 10}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:10,399] Trial 34 finished with value: 0.8160051216389246 and parameters: {'n_estimators': 261, 'max_depth': 20, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:10,835] Trial 35 finished with value: 0.8272136314389836 and parameters: {'n_estimators': 128, 'max_depth': 5, 'min_samples_split': 9}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:11,242] Trial 36 finished with value: 0.8117994681374963 and parameters: {'n_estimators': 103, 'max_depth': 18, 'min_samples_split': 7}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:11,872] Trial 37 finished with value: 0.8188023244361272 and parameters: {'n_estimators': 154, 'max_depth': 11, 'min_samples_split': 5}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:12,595] Trial 38 finished with value: 0.824386880724909 and parameters: {'n_estimators': 209, 'max_depth': 6, 'min_samples_split': 3}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:13,214] Trial 39 finished with value: 0.8188023244361273 and parameters: {'n_estimators': 142, 'max_depth': 13, 'min_samples_split': 8}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:13,850] Trial 40 finished with value: 0.8257854821235103 and parameters: {'n_estimators': 170, 'max_depth': 7, 'min_samples_split': 10}. Best is trial 3 with value: 0.8328277356446371.
    [I 2024-12-06 13:08:14,318] Trial 41 finished with value: 0.8328572835615089 and parameters: {'n_estimators': 112, 'max_depth': 7, 'min_samples_split': 2}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:15,113] Trial 42 finished with value: 0.8286319314488327 and parameters: {'n_estimators': 126, 'max_depth': 8, 'min_samples_split': 2}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:16,833] Trial 43 finished with value: 0.8258248793460062 and parameters: {'n_estimators': 364, 'max_depth': 5, 'min_samples_split': 4}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:17,410] Trial 44 finished with value: 0.817374175120654 and parameters: {'n_estimators': 118, 'max_depth': 9, 'min_samples_split': 3}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:18,030] Trial 45 finished with value: 0.8257953314291342 and parameters: {'n_estimators': 167, 'max_depth': 6, 'min_samples_split': 2}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:18,614] Trial 46 finished with value: 0.8286220821432089 and parameters: {'n_estimators': 145, 'max_depth': 7, 'min_samples_split': 4}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:19,030] Trial 47 finished with value: 0.8258051807347583 and parameters: {'n_estimators': 100, 'max_depth': 8, 'min_samples_split': 3}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:19,841] Trial 48 finished with value: 0.8229882793263075 and parameters: {'n_estimators': 230, 'max_depth': 9, 'min_samples_split': 9}. Best is trial 41 with value: 0.8328572835615089.
    [I 2024-12-06 13:08:20,482] Trial 49 finished with value: 0.8243967300305328 and parameters: {'n_estimators': 186, 'max_depth': 5, 'min_samples_split': 2}. Best is trial 41 with value: 0.8328572835615089.



```python
# Print the best hyperparameters and score
print("Best Parameters:", study.best_params)
print("Best Score:", study.best_value)
```

    Best Parameters: {'n_estimators': 112, 'max_depth': 7, 'min_samples_split': 2}
    Best Score: 0.8328572835615089



```python
# Train the model with the best parameters
best_params = study.best_params
best_model = RandomForestClassifier(**best_params, random_state=42)
best_model.fit(X_train, y_train)
```




<style>#sk-container-id-1 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: black;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-1 {
  color: var(--sklearn-color-text);
}

#sk-container-id-1 pre {
  padding: 0;
}

#sk-container-id-1 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-1 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-1 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-1 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-1 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-1 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-1 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-1 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-1 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-1 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-1 label.sk-toggleable__label {
  cursor: pointer;
  display: block;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
}

#sk-container-id-1 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-1 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-1 div.sk-label label.sk-toggleable__label,
#sk-container-id-1 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-1 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-1 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-1 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-1 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 1ex;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-1 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-1 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-1 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-1 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>RandomForestClassifier(max_depth=7, n_estimators=112, random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;&nbsp;RandomForestClassifier<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestClassifier.html">?<span>Documentation for RandomForestClassifier</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></label><div class="sk-toggleable__content fitted"><pre>RandomForestClassifier(max_depth=7, n_estimators=112, random_state=42)</pre></div> </div></div></div></div>




```python
# Evaluate on the test set
y_pred = best_model.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
```

    Test Accuracy: 0.8100558659217877



```python

```


---
**Score: 15**