---
title: Resume2
date: 2025-01-04
author: Your Name
cell_count: 18
score: 15
---

```python

```


```python
# https://github.com/urchade/GLiNER/blob/main/examples/finetune.ipynb
```


```python
!pip show accelerate
```

    Name: accelerate
    Version: 1.1.1
    Summary: Accelerate
    Home-page: https://github.com/huggingface/accelerate
    Author: The HuggingFace team
    Author-email: zach.mueller@huggingface.co
    License: Apache
    Location: /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages
    Requires: huggingface-hub, numpy, packaging, psutil, pyyaml, safetensors, torch
    Required-by: peft



```python
!wget -P ~/datasets/. https://huggingface.co/datasets/urchade/synthetic-pii-ner-mistral-v1/resolve/main/data.json
```

    --2024-11-20 15:14:13--  https://huggingface.co/datasets/urchade/synthetic-pii-ner-mistral-v1/resolve/main/data.json
    Resolving huggingface.co (huggingface.co)... 54.230.27.69, 54.230.27.75, 54.230.27.119, ...
    Connecting to huggingface.co (huggingface.co)|54.230.27.69|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://cdn-lfs-us-1.hf.co/repos/57/a8/57a8ec4f4ec288845876da262e329709a3abab15f5604211687806ff1c31f16f/78680af45ca6b1175c502db2eec441933de7383f440fc0f0bae46a72be13c0c7?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27data.json%3B+filename%3D%22data.json%22%3B&response-content-type=application%2Fjson&Expires=1732355053&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczMjM1NTA1M319LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzU3L2E4LzU3YThlYzRmNGVjMjg4ODQ1ODc2ZGEyNjJlMzI5NzA5YTNhYmFiMTVmNTYwNDIxMTY4NzgwNmZmMWMzMWYxNmYvNzg2ODBhZjQ1Y2E2YjExNzVjNTAyZGIyZWVjNDQxOTMzZGU3MzgzZjQ0MGZjMGYwYmFlNDZhNzJiZTEzYzBjNz9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=E5rpSeFAbhWY88-sU9Q9Q5XrWFwJEZqlORGLShqEAjo3PNPECF9NNAUiIzW7xaIfnbmof9V8wBjb3p3VR5bGubmZ6j0s2R1-QiiNPACr0SCm6twXLnykhGKAjovku1U4yUjqqBuXRUTZ5irqdVxGHC%7EzhLAmhTGe2w422c1atWiJw9vNTwLymbenetBA%7Egott-agYiRJgboV-qG5P3oyBFK0CzKwS5mbK0HVRSXw4-SI4vCXipiUrbYNU29-5Oktu2nzlXuRMip390v274wWWTMYY1sjUW6VZnXnzvIgR%7ERQH-jbtUd7YgXYsDJsgMtwfUlpT1QXYBDH7BDN%7ENXv0g__&Key-Pair-Id=K24J24Z295AEI9 [following]
    --2024-11-20 15:14:13--  https://cdn-lfs-us-1.hf.co/repos/57/a8/57a8ec4f4ec288845876da262e329709a3abab15f5604211687806ff1c31f16f/78680af45ca6b1175c502db2eec441933de7383f440fc0f0bae46a72be13c0c7?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27data.json%3B+filename%3D%22data.json%22%3B&response-content-type=application%2Fjson&Expires=1732355053&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczMjM1NTA1M319LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzU3L2E4LzU3YThlYzRmNGVjMjg4ODQ1ODc2ZGEyNjJlMzI5NzA5YTNhYmFiMTVmNTYwNDIxMTY4NzgwNmZmMWMzMWYxNmYvNzg2ODBhZjQ1Y2E2YjExNzVjNTAyZGIyZWVjNDQxOTMzZGU3MzgzZjQ0MGZjMGYwYmFlNDZhNzJiZTEzYzBjNz9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=E5rpSeFAbhWY88-sU9Q9Q5XrWFwJEZqlORGLShqEAjo3PNPECF9NNAUiIzW7xaIfnbmof9V8wBjb3p3VR5bGubmZ6j0s2R1-QiiNPACr0SCm6twXLnykhGKAjovku1U4yUjqqBuXRUTZ5irqdVxGHC%7EzhLAmhTGe2w422c1atWiJw9vNTwLymbenetBA%7Egott-agYiRJgboV-qG5P3oyBFK0CzKwS5mbK0HVRSXw4-SI4vCXipiUrbYNU29-5Oktu2nzlXuRMip390v274wWWTMYY1sjUW6VZnXnzvIgR%7ERQH-jbtUd7YgXYsDJsgMtwfUlpT1QXYBDH7BDN%7ENXv0g__&Key-Pair-Id=K24J24Z295AEI9
    Resolving cdn-lfs-us-1.hf.co (cdn-lfs-us-1.hf.co)... 18.172.64.104, 18.172.64.30, 18.172.64.13, ...
    Connecting to cdn-lfs-us-1.hf.co (cdn-lfs-us-1.hf.co)|18.172.64.104|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 23300735 (22M) [application/json]
    Saving to: ‘/home/rajaraman/datasets/./data.json’
    
    data.json           100%[===================>]  22.22M  11.5MB/s    in 1.9s    
    
    2024-11-20 15:14:16 (11.5 MB/s) - ‘/home/rajaraman/datasets/./data.json’ saved [23300735/23300735]
    



```python
!ls ~/datasets/gliner-data.json
```

    /home/rajaraman/datasets/gliner-data.json



```python
# !source ~/.zshrc
```


```python
import json
import random
```


```python
train_path = "/home/rajaraman/datasets/gliner-data.json"

with open(train_path, "r") as f:
    data = json.load(f)

print('Dataset size:', len(data))

random.shuffle(data)
print('Dataset is shuffled...')

train_dataset = data[:int(len(data)*0.9)]
test_dataset = data[int(len(data)*0.9):]

print('Dataset is splitted...')
```

    Dataset size: 19635
    Dataset is shuffled...
    Dataset is splitted...



```python
!pip show keras
```

    Name: keras
    Version: 3.6.0
    Summary: Multi-backend Keras.
    Home-page: https://github.com/keras-team/keras
    Author: Keras team
    Author-email: keras-users@googlegroups.com
    License: Apache License 2.0
    Location: /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages
    Requires: absl-py, h5py, ml-dtypes, namex, numpy, optree, packaging, rich
    Required-by: tensorflow



```python
# !pip install keras
```


```python
#!pip install tf-keras
```


```python
!pip show tf-keras
```

    Name: tf_keras
    Version: 2.18.0
    Summary: Deep learning for humans.
    Home-page: https://keras.io/
    Author: Keras team
    Author-email: keras-users@googlegroups.com
    License: Apache 2.0
    Location: /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages
    Requires: tensorflow
    Required-by: 



```python
import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"

import torch
from gliner import GLiNERConfig, GLiNER
from gliner.training import Trainer, TrainingArguments
from gliner.data_processing.collator import DataCollatorWithPadding, DataCollator
from gliner.utils import load_config_as_namespace
from gliner.data_processing import WordsSplitter, GLiNERDataset
```


```python
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

model = GLiNER.from_pretrained("urchade/gliner_small")
```


    Fetching 4 files:   0%|          | 0/4 [00:00<?, ?it/s]



    gliner_config.json:   0%|          | 0.00/477 [00:00<?, ?B/s]



    pytorch_model.bin:   0%|          | 0.00/611M [00:00<?, ?B/s]



    .gitattributes:   0%|          | 0.00/1.52k [00:00<?, ?B/s]



    README.md:   0%|          | 0.00/4.84k [00:00<?, ?B/s]



    tokenizer_config.json:   0%|          | 0.00/52.0 [00:00<?, ?B/s]



    config.json:   0%|          | 0.00/578 [00:00<?, ?B/s]



    spm.model:   0%|          | 0.00/2.46M [00:00<?, ?B/s]


    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/convert_slow_tokenizer.py:562: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
      warnings.warn(



```python
# use it for better performance, it mimics original implementation but it's less memory efficient
data_collator = DataCollator(model.config, data_processor=model.data_processor, prepare_labels=True)
```


```python
# Optional: compile model for faster training
model.to(device)
print("done")
```

    done



```python
# calculate number of epochs
num_steps = 500
batch_size = 8
data_size = len(train_dataset)
num_batches = data_size // batch_size
num_epochs = max(1, num_steps // num_batches)

training_args = TrainingArguments(
    output_dir="models",
    learning_rate=5e-6,
    weight_decay=0.01,
    others_lr=1e-5,
    others_weight_decay=0.01,
    lr_scheduler_type="linear", #cosine
    warmup_ratio=0.1,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    focal_loss_alpha=0.75,
    focal_loss_gamma=2,
    num_train_epochs=num_epochs,
    evaluation_strategy="steps",
    save_steps = 100,
    save_total_limit=10,
    dataloader_num_workers = 0,
    use_cpu = False,
    report_to="none",
    )

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=model.data_processor.transformer_tokenizer,
    data_collator=data_collator,
)

# trainer.train()
```

    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/training_args.py:1494: FutureWarning: `evaluation_strategy` is deprecated and will be removed in version 4.46 of 🤗 Transformers. Use `eval_strategy` instead
      warnings.warn(



```python

```


---
**Score: 15**