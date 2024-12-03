---
title: Census-Data
date: 2024-12-04
author: Your Name
cell_count: 31
score: 30
---

---
title: "Census Data and Linear Classifier"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
import tensorflow as tf

import os

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```


```python
import numpy as np
import pandas as pd
```


```python
census = pd.read_csv("/Users/rajacsp/datasets/census_data.csv")
```


```python
census.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>education</th>
      <th>education_num</th>
      <th>marital_status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>gender</th>
      <th>capital_gain</th>
      <th>capital_loss</th>
      <th>hours_per_week</th>
      <th>native_country</th>
      <th>income_bracket</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>State-gov</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Never-married</td>
      <td>Adm-clerical</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>2174</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>Self-emp-not-inc</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>2</th>
      <td>38</td>
      <td>Private</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Divorced</td>
      <td>Handlers-cleaners</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53</td>
      <td>Private</td>
      <td>11th</td>
      <td>7</td>
      <td>Married-civ-spouse</td>
      <td>Handlers-cleaners</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>4</th>
      <td>28</td>
      <td>Private</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Wife</td>
      <td>Black</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>Cuba</td>
      <td>&lt;=50K</td>
    </tr>
  </tbody>
</table>
</div>




```python
census['income_bracket'].unique()
```




    array([' <=50K', ' >50K'], dtype=object)




```python
# Fix the income bracket
def label_fix(label):
    label = label.strip().lower()
    if(label == '<=50k'):
        return 0
    return 1
        
```


```python
census['income_bracket'] = census['income_bracket'].apply(label_fix)
```


```python
census['income_bracket'].unique()
```




    array([0, 1])




```python
# Train Test Split
from sklearn.model_selection import train_test_split


```


```python
x_data = census.drop('income_bracket', axis=1)
y_labels = census['income_bracket']

X_train, x_test, y_train, y_est = train_test_split(x_data, y_labels, test_size=0.3, random_state=101)
```


```python
census.columns
```




    Index(['age', 'workclass', 'education', 'education_num', 'marital_status',
           'occupation', 'relationship', 'race', 'gender', 'capital_gain',
           'capital_loss', 'hours_per_week', 'native_country', 'income_bracket'],
          dtype='object')




```python
import tensorflow as tf
from tensorflow.feature_column import categorical_column_with_vocabulary_list as vlist
```


```python
gender = vlist("gender", ["Female", "Male"])
```


```python
gender
```




    VocabularyListCategoricalColumn(key='gender', vocabulary_list=('Female', 'Male'), dtype=tf.string, default_value=-1, num_oov_buckets=0)




```python
from tensorflow.feature_column import categorical_column_with_hash_bucket as bucket
```


```python
occupation = bucket("occupation", hash_bucket_size=1000)
marital_status = bucket("marital_status", hash_bucket_size=1000)
relationship = bucket("relationship", hash_bucket_size=1000)
education = bucket("education", hash_bucket_size=1000)
workclass = bucket("workclass", hash_bucket_size=1000)
native_country = bucket("native_country", hash_bucket_size=1000)
```


```python
from tensorflow.feature_column import numeric_column as nc
```


```python
age = nc("age")
education_num = nc("education_num")
capital_gain = nc("capital_gain")
capital_loss = nc("capital_loss")
hours_per_week = nc("hours_per_week")
```


```python
feat_cols = [gender, occupation, marital_status, relationship, education, workclass, native_country, age, education_num, 
            capital_gain, capital_loss, hours_per_week]
```


```python
feat_cols
```




    [VocabularyListCategoricalColumn(key='gender', vocabulary_list=('Female', 'Male'), dtype=tf.string, default_value=-1, num_oov_buckets=0),
     HashedCategoricalColumn(key='occupation', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='marital_status', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='relationship', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='education', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='workclass', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='native_country', hash_bucket_size=1000, dtype=tf.string),
     NumericColumn(key='age', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='education_num', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='capital_gain', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='capital_loss', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='hours_per_week', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None)]




```python
input_func = tf.estimator.inputs.pandas_input_fn(x=X_train, y = y_train, batch_size=100, num_epochs=None, shuffle=True)
```


```python
model = tf.estimator.LinearClassifier(feature_columns=feat_cols)
```

    INFO:tensorflow:Using default config.
    WARNING:tensorflow:Using temporary folder as model directory: /var/folders/fk/b_m_3t9915zc2llvfkwd4d_h0000gn/T/tmp3xkmlm9h
    INFO:tensorflow:Using config: {'_model_dir': '/var/folders/fk/b_m_3t9915zc2llvfkwd4d_h0000gn/T/tmp3xkmlm9h', '_tf_random_seed': None, '_save_summary_steps': 100, '_save_checkpoints_steps': None, '_save_checkpoints_secs': 600, '_session_config': allow_soft_placement: true
    graph_options {
      rewrite_options {
        meta_optimizer_iterations: ONE
      }
    }
    , '_keep_checkpoint_max': 5, '_keep_checkpoint_every_n_hours': 10000, '_log_step_count_steps': 100, '_train_distribute': None, '_device_fn': None, '_protocol': None, '_eval_distribute': None, '_experimental_distribute': None, '_service': None, '_cluster_spec': <tensorflow.python.training.server_lib.ClusterSpec object at 0x130e60e80>, '_task_type': 'worker', '_task_id': 0, '_global_id_in_cluster': 0, '_master': '', '_evaluation_master': '', '_is_chief': True, '_num_ps_replicas': 0, '_num_worker_replicas': 1}



```python
model.train(input_fn=input_func, steps=5000)
```

    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Colocations handled automatically by placer.
    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow_estimator/python/estimator/inputs/queues/feeding_queue_runner.py:62: QueueRunner.__init__ (from tensorflow.python.training.queue_runner_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    To construct input pipelines, use the `tf.data` module.
    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow_estimator/python/estimator/inputs/queues/feeding_functions.py:500: add_queue_runner (from tensorflow.python.training.queue_runner_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    To construct input pipelines, use the `tf.data` module.
    INFO:tensorflow:Calling model_fn.
    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow/python/feature_column/feature_column_v2.py:2703: to_float (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use tf.cast instead.
    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow/python/ops/lookup_ops.py:1137: to_int64 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use tf.cast instead.
    INFO:tensorflow:Done calling model_fn.
    INFO:tensorflow:Create CheckpointSaverHook.
    INFO:tensorflow:Graph was finalized.
    INFO:tensorflow:Running local_init_op.
    INFO:tensorflow:Done running local_init_op.
    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow/python/training/monitored_session.py:809: start_queue_runners (from tensorflow.python.training.queue_runner_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    To construct input pipelines, use the `tf.data` module.
    INFO:tensorflow:Saving checkpoints for 0 into /var/folders/fk/b_m_3t9915zc2llvfkwd4d_h0000gn/T/tmp3xkmlm9h/model.ckpt.
    INFO:tensorflow:loss = 69.31472, step = 1
    INFO:tensorflow:global_step/sec: 183.162
    INFO:tensorflow:loss = 74.34316, step = 101 (0.549 sec)
    INFO:tensorflow:global_step/sec: 282.272
    INFO:tensorflow:loss = 258.81635, step = 201 (0.354 sec)
    INFO:tensorflow:global_step/sec: 360.103
    INFO:tensorflow:loss = 92.93664, step = 301 (0.277 sec)
    INFO:tensorflow:global_step/sec: 310.323
    INFO:tensorflow:loss = 479.21606, step = 401 (0.323 sec)
    INFO:tensorflow:global_step/sec: 363.822
    INFO:tensorflow:loss = 64.496826, step = 501 (0.273 sec)
    INFO:tensorflow:global_step/sec: 287.337
    INFO:tensorflow:loss = 142.80907, step = 601 (0.349 sec)
    INFO:tensorflow:global_step/sec: 329.981
    INFO:tensorflow:loss = 158.61514, step = 701 (0.303 sec)
    INFO:tensorflow:global_step/sec: 361.742
    INFO:tensorflow:loss = 92.889305, step = 801 (0.276 sec)
    INFO:tensorflow:global_step/sec: 336.053
    INFO:tensorflow:loss = 47.939163, step = 901 (0.298 sec)
    INFO:tensorflow:global_step/sec: 386.539
    INFO:tensorflow:loss = 109.61961, step = 1001 (0.258 sec)
    INFO:tensorflow:global_step/sec: 349.966
    INFO:tensorflow:loss = 97.20078, step = 1101 (0.287 sec)
    INFO:tensorflow:global_step/sec: 367.692
    INFO:tensorflow:loss = 102.36524, step = 1201 (0.272 sec)
    INFO:tensorflow:global_step/sec: 386.157
    INFO:tensorflow:loss = 97.24974, step = 1301 (0.258 sec)
    INFO:tensorflow:global_step/sec: 426.666
    INFO:tensorflow:loss = 106.33708, step = 1401 (0.234 sec)
    INFO:tensorflow:global_step/sec: 390.189
    INFO:tensorflow:loss = 88.20786, step = 1501 (0.258 sec)
    INFO:tensorflow:global_step/sec: 392.219
    INFO:tensorflow:loss = 40.560345, step = 1601 (0.254 sec)
    INFO:tensorflow:global_step/sec: 408.792
    INFO:tensorflow:loss = 67.237366, step = 1701 (0.243 sec)
    INFO:tensorflow:global_step/sec: 392.664
    INFO:tensorflow:loss = 100.42717, step = 1801 (0.257 sec)
    INFO:tensorflow:global_step/sec: 391.489
    INFO:tensorflow:loss = 104.48391, step = 1901 (0.254 sec)
    INFO:tensorflow:global_step/sec: 346.702
    INFO:tensorflow:loss = 30.307816, step = 2001 (0.289 sec)
    INFO:tensorflow:global_step/sec: 381.499
    INFO:tensorflow:loss = 41.16053, step = 2101 (0.261 sec)
    INFO:tensorflow:global_step/sec: 292.709
    INFO:tensorflow:loss = 73.87081, step = 2201 (0.342 sec)
    INFO:tensorflow:global_step/sec: 341.69
    INFO:tensorflow:loss = 42.253674, step = 2301 (0.295 sec)
    INFO:tensorflow:global_step/sec: 333.577
    INFO:tensorflow:loss = 32.43901, step = 2401 (0.300 sec)
    INFO:tensorflow:global_step/sec: 380.409
    INFO:tensorflow:loss = 37.70379, step = 2501 (0.262 sec)
    INFO:tensorflow:global_step/sec: 340.751
    INFO:tensorflow:loss = 39.260693, step = 2601 (0.294 sec)
    INFO:tensorflow:global_step/sec: 291.395
    INFO:tensorflow:loss = 51.416866, step = 2701 (0.343 sec)
    INFO:tensorflow:global_step/sec: 315.53
    INFO:tensorflow:loss = 184.38156, step = 2801 (0.316 sec)
    INFO:tensorflow:global_step/sec: 366.986
    INFO:tensorflow:loss = 53.05883, step = 2901 (0.272 sec)
    INFO:tensorflow:global_step/sec: 265.167
    INFO:tensorflow:loss = 27.692787, step = 3001 (0.380 sec)
    INFO:tensorflow:global_step/sec: 339.134
    INFO:tensorflow:loss = 39.770794, step = 3101 (0.292 sec)
    INFO:tensorflow:global_step/sec: 358.485
    INFO:tensorflow:loss = 47.001534, step = 3201 (0.279 sec)
    INFO:tensorflow:global_step/sec: 281.97
    INFO:tensorflow:loss = 36.61994, step = 3301 (0.356 sec)
    INFO:tensorflow:global_step/sec: 343.422
    INFO:tensorflow:loss = 46.674873, step = 3401 (0.289 sec)
    INFO:tensorflow:global_step/sec: 281.989
    INFO:tensorflow:loss = 36.499893, step = 3501 (0.356 sec)
    INFO:tensorflow:global_step/sec: 352.627
    INFO:tensorflow:loss = 44.82026, step = 3601 (0.282 sec)
    INFO:tensorflow:global_step/sec: 357.209
    INFO:tensorflow:loss = 109.4581, step = 3701 (0.280 sec)
    INFO:tensorflow:global_step/sec: 289.537
    INFO:tensorflow:loss = 52.670895, step = 3801 (0.349 sec)
    INFO:tensorflow:global_step/sec: 337.938
    INFO:tensorflow:loss = 25.518808, step = 3901 (0.294 sec)
    INFO:tensorflow:global_step/sec: 326.968
    INFO:tensorflow:loss = 88.96236, step = 4001 (0.306 sec)
    INFO:tensorflow:global_step/sec: 335.375
    INFO:tensorflow:loss = 34.12282, step = 4101 (0.296 sec)
    INFO:tensorflow:global_step/sec: 330.084
    INFO:tensorflow:loss = 26.477894, step = 4201 (0.304 sec)
    INFO:tensorflow:global_step/sec: 342.657
    INFO:tensorflow:loss = 58.477943, step = 4301 (0.292 sec)
    INFO:tensorflow:global_step/sec: 320.761
    INFO:tensorflow:loss = 109.7404, step = 4401 (0.313 sec)
    INFO:tensorflow:global_step/sec: 322.263
    INFO:tensorflow:loss = 70.80423, step = 4501 (0.309 sec)
    INFO:tensorflow:global_step/sec: 276.567
    INFO:tensorflow:loss = 42.813023, step = 4601 (0.362 sec)
    INFO:tensorflow:global_step/sec: 335.875
    INFO:tensorflow:loss = 50.28676, step = 4701 (0.296 sec)
    INFO:tensorflow:global_step/sec: 263.377
    INFO:tensorflow:loss = 69.291405, step = 4801 (0.382 sec)
    INFO:tensorflow:global_step/sec: 297.762
    INFO:tensorflow:loss = 112.38106, step = 4901 (0.336 sec)
    INFO:tensorflow:Saving checkpoints for 5000 into /var/folders/fk/b_m_3t9915zc2llvfkwd4d_h0000gn/T/tmp3xkmlm9h/model.ckpt.
    INFO:tensorflow:Loss for final step: 32.800762.





    <tensorflow_estimator.python.estimator.canned.linear.LinearClassifier at 0x130e60940>




```python
# Evaluation

pred_fn = tf.estimator.inputs.pandas_input_fn(x=x_test, batch_size=len(x_test), shuffle=False)
```


```python
prediction = list(model.predict(input_fn=pred_fn))
```

    INFO:tensorflow:Calling model_fn.
    INFO:tensorflow:Done calling model_fn.
    INFO:tensorflow:Graph was finalized.
    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow/python/training/saver.py:1266: checkpoint_exists (from tensorflow.python.training.checkpoint_management) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use standard file APIs to check for files with this prefix.
    INFO:tensorflow:Restoring parameters from /var/folders/fk/b_m_3t9915zc2llvfkwd4d_h0000gn/T/tmp3xkmlm9h/model.ckpt-5000
    INFO:tensorflow:Running local_init_op.
    INFO:tensorflow:Done running local_init_op.



```python
prediction[0]
```




    {'class_ids': array([0]),
     'classes': array([b'0'], dtype=object),
     'logistic': array([0.24731174], dtype=float32),
     'logits': array([-1.1130015], dtype=float32),
     'probabilities': array([0.7526882 , 0.24731174], dtype=float32)}




```python
final_preds = []

for pred in prediction:
    final_preds.append(pred['class_ids'][0])
```


```python
final_preds[:10]
```




    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]




```python
from sklearn.metrics import classification_report
```


```python
print(classification_report(y_est, final_preds))
```

                  precision    recall  f1-score   support
    
               0       0.86      0.93      0.89      7436
               1       0.70      0.54      0.61      2333
    
       micro avg       0.83      0.83      0.83      9769
       macro avg       0.78      0.73      0.75      9769
    weighted avg       0.83      0.83      0.83      9769
    



---
**Score: 30**