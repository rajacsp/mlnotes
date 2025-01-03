---
title: Address-Analysis-With-Hf
date: 2025-01-03
author: Your Name
cell_count: 9
score: 5
---

```python
# !pip install datasets
```


```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset
```


```python
# Load data
dataset = load_dataset("json", data_files="train_data.json")
```


    Generating train split: 0 examples [00:00, ? examples/s]



```python
dataset
```




    DatasetDict({
        train: Dataset({
            features: ['text', 'entities'],
            num_rows: 1
        })
    })




```python
# Load model and tokenizer
# model = AutoModelForTokenClassification.from_pretrained("urchade/gliner_medium-v2.1")
# tokenizer = AutoTokenizer.from_pretrained("urchade/gliner_medium-v2.1")
```


```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, AutoConfig
```


```python
# Path to the local model directory
model_dir = "/home/rajaraman/datasets/gliner/gliner_medium-v2.1"
```


```python
# Load the configuration manually
config = AutoConfig.from_pretrained(f"{model_dir}/gliner_config.json", local_files_only=True)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[14], line 2
          1 # Load the configuration manually
    ----> 2 config = AutoConfig.from_pretrained(f"{model_dir}/gliner_config.json", local_files_only=True)


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/models/auto/configuration_auto.py:997, in AutoConfig.from_pretrained(cls, pretrained_model_name_or_path, **kwargs)
        994         if pattern in str(pretrained_model_name_or_path):
        995             return CONFIG_MAPPING[pattern].from_dict(config_dict, **unused_kwargs)
    --> 997 raise ValueError(
        998     f"Unrecognized model in {pretrained_model_name_or_path}. "
        999     f"Should have a `model_type` key in its {CONFIG_NAME}, or contain one of the following strings "
       1000     f"in its name: {', '.join(CONFIG_MAPPING.keys())}"
       1001 )


    ValueError: Unrecognized model in /home/rajaraman/datasets/gliner/gliner_medium-v2.1/gliner_config.json. Should have a `model_type` key in its config.json, or contain one of the following strings in its name: albert, align, altclip, audio-spectrogram-transformer, autoformer, bark, bart, beit, bert, bert-generation, big_bird, bigbird_pegasus, biogpt, bit, blenderbot, blenderbot-small, blip, blip-2, bloom, bridgetower, bros, camembert, canine, chinese_clip, chinese_clip_vision_model, clap, clip, clip_vision_model, clipseg, clvp, code_llama, codegen, cohere, conditional_detr, convbert, convnext, convnextv2, cpmant, ctrl, cvt, data2vec-audio, data2vec-text, data2vec-vision, dbrx, deberta, deberta-v2, decision_transformer, deformable_detr, deit, depth_anything, deta, detr, dinat, dinov2, distilbert, donut-swin, dpr, dpt, efficientformer, efficientnet, electra, encodec, encoder-decoder, ernie, ernie_m, esm, falcon, fastspeech2_conformer, flaubert, flava, fnet, focalnet, fsmt, funnel, fuyu, gemma, gemma2, git, glpn, gpt-sw3, gpt2, gpt_bigcode, gpt_neo, gpt_neox, gpt_neox_japanese, gptj, gptsan-japanese, graphormer, grounding-dino, groupvit, hubert, ibert, idefics, idefics2, imagegpt, informer, instructblip, instructblipvideo, jamba, jetmoe, jukebox, kosmos-2, layoutlm, layoutlmv2, layoutlmv3, led, levit, lilt, llama, llava, llava-next-video, llava_next, longformer, longt5, luke, lxmert, m2m_100, mamba, marian, markuplm, mask2former, maskformer, maskformer-swin, mbart, mctct, mega, megatron-bert, mgp-str, mistral, mixtral, mobilebert, mobilenet_v1, mobilenet_v2, mobilevit, mobilevitv2, mpnet, mpt, mra, mt5, musicgen, musicgen_melody, mvp, nat, nezha, nllb-moe, nougat, nystromformer, olmo, oneformer, open-llama, openai-gpt, opt, owlv2, owlvit, paligemma, patchtsmixer, patchtst, pegasus, pegasus_x, perceiver, persimmon, phi, phi3, pix2struct, plbart, poolformer, pop2piano, prophetnet, pvt, pvt_v2, qdqbert, qwen2, qwen2_moe, rag, realm, recurrent_gemma, reformer, regnet, rembert, resnet, retribert, roberta, roberta-prelayernorm, roc_bert, roformer, rt_detr, rt_detr_resnet, rwkv, sam, seamless_m4t, seamless_m4t_v2, segformer, seggpt, sew, sew-d, siglip, siglip_vision_model, speech-encoder-decoder, speech_to_text, speech_to_text_2, speecht5, splinter, squeezebert, stablelm, starcoder2, superpoint, swiftformer, swin, swin2sr, swinv2, switch_transformers, t5, table-transformer, tapas, time_series_transformer, timesformer, timm_backbone, trajectory_transformer, transfo-xl, trocr, tvlt, tvp, udop, umt5, unispeech, unispeech-sat, univnet, upernet, van, video_llava, videomae, vilt, vipllava, vision-encoder-decoder, vision-text-dual-encoder, visual_bert, vit, vit_hybrid, vit_mae, vit_msn, vitdet, vitmatte, vits, vivit, wav2vec2, wav2vec2-bert, wav2vec2-conformer, wavlm, whisper, xclip, xglm, xlm, xlm-prophetnet, xlm-roberta, xlm-roberta-xl, xlnet, xmod, yolos, yoso



```python

```


---
**Score: 5**