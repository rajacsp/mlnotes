---
title: Resume-1
date: 2025-05-17
author: Your Name
cell_count: 18
score: 15
---

```python
!python --version
```

    Python 3.12.4



```python
!pip show PyPDF2 spacy gliner | grep "Version"
```

    Version: 3.0.1
    Version: 3.8.2
    Version: 0.2.13



```python

```


```python
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text
```


```python
from gliner import GLiNER
```


```python
# Initialize GLiNER with a pre-trained model
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")
```


    Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]


    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/convert_slow_tokenizer.py:562: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
      warnings.warn(



```python
# Extract text from the resume PDF
pdf_path = "aravindhan-resume.pdf"  # Replace with your PDF file path
resume_text = extract_text_from_pdf(pdf_path)
```


```python
resume_text
```




    '                                          A.ARAVINDHAN  \n\uf0299962962450  \nAddress:No41  Kalaigar Nagar 6th Street Manali ,Chennai -600068  \n@A.Aravindhananta @gmail.com  \nEducation Qualification:  \nSSLC: Government Higher Secondary School Manali ,Chennai -600068  \nState Board  \nPassing year:2017  \nHSC: Government Higher Secondary School Manali ,Chennai -600068  \nState Board  \nPassing Year:2019  \nDEGREE OF COURSE (UG):  \nB.Sc(Computer Science)  \nJ.H.A Agarsen College Madhavaram, Chennai -600060  \nPassing Year:2022  \nAchievements:  \n\uf0d8 Won cricket  Championship in Inter -school  and Outer school \nCompetition(2017 -2018 ) \n\uf0d8 Won volley ball  Championship in Inter -school  and Outer school \nCompetition(2018 -2019 ) \n\uf0d8  \nPersonal Skills:  \n\uf0d8 Positive Thinking  \n\uf0d8 Make Friendship Easily  \n\uf0d8 Good Speaker  \n\uf0d8 Quick Learner  \uf0d8 Good Learner  \nSkills:  \n\uf0d8 Python  \n\uf0d8 Html  \n\uf0d8 Django  \n\uf0d8 MySQL \n\uf0d8 Computer Knowledge  \nLanguage Known:  \n\uf0d8 Read : Tamil,English  \n\uf0d8 Write: Tamil,English  \n\uf0d8 Speak : Tamil,English  \nBio Data:  \n      Name                :   A.Aravindhan  \n      Father Name    :  M.Aanadhan  \n      Gender               :  Male  \n      Marital Status   :  Single  \n      Nationality        :   Indian  \nDeclaration:  \nI here by declare that the above written particulars are true to the best of my \nKnowledge and belief.  \n \nPlace:  \nDate:                                                                                                               Signature  \n    '




```python
# Define the tech-related labels (customized for tech keys)
labels = ["TECH_KEY"]
```


```python
# Perform entity prediction
tech_keys = model.predict_entities(resume_text, labels, threshold=0.5)
```

    Asking to truncate to max_length but no maximum length is provided and the model has no predefined maximum length. Default to no truncation.



```python
# Extract only the tech keys
extracted_tech_keys = {key['text'] for key in tech_keys}
```


```python
# Display the results
print("Extracted Tech Keys:")
for tech in extracted_tech_keys:
    print(tech)
```

    Extracted Tech Keys:



```python

```


```python

```


```python
# Paths to training data and output directory
train_data_path = "train_data.json"  # Path to your training dataset
output_dir = "model_output_dir"      # Path to save the trained model
```


```python
help(GLiNER.train)
```

    Help on function train in module torch.nn.modules.module:
    
    train(self: ~T, mode: bool = True) -> ~T
        Set the module in training mode.
    
        This has any effect only on certain modules. See documentations of
        particular modules for details of their behaviors in training/evaluation
        mode, if they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
        etc.
    
        Args:
            mode (bool): whether to set training mode (``True``) or evaluation
                         mode (``False``). Default: ``True``.
    
        Returns:
            Module: self
    



```python
# https://github.com/urchade/GLiNER/blob/main/examples/finetune.ipynb
```


```python

```


---
**Score: 15**