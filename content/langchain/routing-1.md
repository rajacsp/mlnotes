---
title: Routing-1
date: 2025-01-03
author: Your Name
cell_count: 16
score: 15
---

9
<br>How to: route between sub-chains
<br>https://python.langchain.com/docs/how_to/routing/


```python
!python --version
```

    Python 3.12.4



```python
from constants import OPENAI_API_KEY
```


```python
!pip show langchain-openai | grep "Version:"
```

    Version: 0.2.9



```python
import os
```


```python
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```


```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
```


```python
#!pip install langchain_anthropic
```


```python
from langchain_anthropic import ChatAnthropic
```


```python
from langchain_community.utils.math import cosine_similarity
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

physics_template = """You are a very smart physics professor. \
You are great at answering questions about physics in a concise and easy to understand manner. \
When you don't know the answer to a question you admit that you don't know.

Here is a question:
{query}"""

math_template = """You are a very good mathematician. You are great at answering math questions. \
You are so good because you are able to break down hard problems into their component parts, \
answer the component parts, and then put them together to answer the broader question.

Here is a question:
{query}"""

embeddings = OpenAIEmbeddings()
prompt_templates = [physics_template, math_template]
prompt_embeddings = embeddings.embed_documents(prompt_templates)


def prompt_router(input):
    query_embedding = embeddings.embed_query(input["query"])
    similarity = cosine_similarity([query_embedding], prompt_embeddings)[0]
    most_similar = prompt_templates[similarity.argmax()]
    print("Using MATH" if most_similar == math_template else "Using PHYSICS")
    return PromptTemplate.from_template(most_similar)


chain = (
    {"query": RunnablePassthrough()}
    | RunnableLambda(prompt_router)
    | ChatAnthropic(model="claude-3-haiku-20240307")
    | StrOutputParser()
)
```


```python
chain.invoke("What's a black hole")
```

    Using PHYSICS



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[33], line 1
    ----> 1 chain.invoke("What's a black hole")


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/langchain_core/runnables/base.py:3024, in RunnableSequence.invoke(self, input, config, **kwargs)
       3022             input = context.run(step.invoke, input, config, **kwargs)
       3023         else:
    -> 3024             input = context.run(step.invoke, input, config)
       3025 # finish the root run
       3026 except BaseException as e:


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/langchain_core/language_models/chat_models.py:286, in BaseChatModel.invoke(self, input, config, stop, **kwargs)
        275 def invoke(
        276     self,
        277     input: LanguageModelInput,
       (...)
        281     **kwargs: Any,
        282 ) -> BaseMessage:
        283     config = ensure_config(config)
        284     return cast(
        285         ChatGeneration,
    --> 286         self.generate_prompt(
        287             [self._convert_input(input)],
        288             stop=stop,
        289             callbacks=config.get("callbacks"),
        290             tags=config.get("tags"),
        291             metadata=config.get("metadata"),
        292             run_name=config.get("run_name"),
        293             run_id=config.pop("run_id", None),
        294             **kwargs,
        295         ).generations[0][0],
        296     ).message


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/langchain_core/language_models/chat_models.py:786, in BaseChatModel.generate_prompt(self, prompts, stop, callbacks, **kwargs)
        778 def generate_prompt(
        779     self,
        780     prompts: list[PromptValue],
       (...)
        783     **kwargs: Any,
        784 ) -> LLMResult:
        785     prompt_messages = [p.to_messages() for p in prompts]
    --> 786     return self.generate(prompt_messages, stop=stop, callbacks=callbacks, **kwargs)


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/langchain_core/language_models/chat_models.py:643, in BaseChatModel.generate(self, messages, stop, callbacks, tags, metadata, run_name, run_id, **kwargs)
        641         if run_managers:
        642             run_managers[i].on_llm_error(e, response=LLMResult(generations=[]))
    --> 643         raise e
        644 flattened_outputs = [
        645     LLMResult(generations=[res.generations], llm_output=res.llm_output)  # type: ignore[list-item]
        646     for res in results
        647 ]
        648 llm_output = self._combine_llm_outputs([res.llm_output for res in results])


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/langchain_core/language_models/chat_models.py:633, in BaseChatModel.generate(self, messages, stop, callbacks, tags, metadata, run_name, run_id, **kwargs)
        630 for i, m in enumerate(messages):
        631     try:
        632         results.append(
    --> 633             self._generate_with_cache(
        634                 m,
        635                 stop=stop,
        636                 run_manager=run_managers[i] if run_managers else None,
        637                 **kwargs,
        638             )
        639         )
        640     except BaseException as e:
        641         if run_managers:


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/langchain_core/language_models/chat_models.py:851, in BaseChatModel._generate_with_cache(self, messages, stop, run_manager, **kwargs)
        849 else:
        850     if inspect.signature(self._generate).parameters.get("run_manager"):
    --> 851         result = self._generate(
        852             messages, stop=stop, run_manager=run_manager, **kwargs
        853         )
        854     else:
        855         result = self._generate(messages, stop=stop, **kwargs)


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/langchain_anthropic/chat_models.py:796, in ChatAnthropic._generate(self, messages, stop, run_manager, **kwargs)
        794     return generate_from_stream(stream_iter)
        795 payload = self._get_request_payload(messages, stop=stop, **kwargs)
    --> 796 data = self._client.messages.create(**payload)
        797 return self._format_output(data, **kwargs)


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/_utils/_utils.py:275, in required_args.<locals>.inner.<locals>.wrapper(*args, **kwargs)
        273             msg = f"Missing required argument: {quote(missing[0])}"
        274     raise TypeError(msg)
    --> 275 return func(*args, **kwargs)


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/resources/messages.py:888, in Messages.create(self, max_tokens, messages, model, metadata, stop_sequences, stream, system, temperature, tool_choice, tools, top_k, top_p, extra_headers, extra_query, extra_body, timeout)
        881 if model in DEPRECATED_MODELS:
        882     warnings.warn(
        883         f"The model '{model}' is deprecated and will reach end-of-life on {DEPRECATED_MODELS[model]}.\nPlease migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.",
        884         DeprecationWarning,
        885         stacklevel=3,
        886     )
    --> 888 return self._post(
        889     "/v1/messages",
        890     body=maybe_transform(
        891         {
        892             "max_tokens": max_tokens,
        893             "messages": messages,
        894             "model": model,
        895             "metadata": metadata,
        896             "stop_sequences": stop_sequences,
        897             "stream": stream,
        898             "system": system,
        899             "temperature": temperature,
        900             "tool_choice": tool_choice,
        901             "tools": tools,
        902             "top_k": top_k,
        903             "top_p": top_p,
        904         },
        905         message_create_params.MessageCreateParams,
        906     ),
        907     options=make_request_options(
        908         extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        909     ),
        910     cast_to=Message,
        911     stream=stream or False,
        912     stream_cls=Stream[RawMessageStreamEvent],
        913 )


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/_base_client.py:1277, in SyncAPIClient.post(self, path, cast_to, body, options, files, stream, stream_cls)
       1263 def post(
       1264     self,
       1265     path: str,
       (...)
       1272     stream_cls: type[_StreamT] | None = None,
       1273 ) -> ResponseT | _StreamT:
       1274     opts = FinalRequestOptions.construct(
       1275         method="post", url=path, json_data=body, files=to_httpx_files(files), **options
       1276     )
    -> 1277     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/_base_client.py:954, in SyncAPIClient.request(self, cast_to, options, remaining_retries, stream, stream_cls)
        951 else:
        952     retries_taken = 0
    --> 954 return self._request(
        955     cast_to=cast_to,
        956     options=options,
        957     stream=stream,
        958     stream_cls=stream_cls,
        959     retries_taken=retries_taken,
        960 )


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/_base_client.py:980, in SyncAPIClient._request(self, cast_to, options, retries_taken, stream, stream_cls)
        977 options = self._prepare_options(options)
        979 remaining_retries = options.get_max_retries(self.max_retries) - retries_taken
    --> 980 request = self._build_request(options, retries_taken=retries_taken)
        981 self._prepare_request(request)
        983 kwargs: HttpxSendArgs = {}


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/_base_client.py:465, in BaseClient._build_request(self, options, retries_taken)
        462     else:
        463         raise RuntimeError(f"Unexpected JSON data type, {type(json_data)}, cannot merge with `extra_body`")
    --> 465 headers = self._build_headers(options, retries_taken=retries_taken)
        466 params = _merge_mappings(self.default_query, options.params)
        467 content_type = headers.get("Content-Type")


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/_base_client.py:413, in BaseClient._build_headers(self, options, retries_taken)
        411 custom_headers = options.headers or {}
        412 headers_dict = _merge_mappings(self.default_headers, custom_headers)
    --> 413 self._validate_headers(headers_dict, custom_headers)
        415 # headers are case-insensitive while dictionaries are not.
        416 headers = httpx.Headers(headers_dict)


    File ~/miniconda3/envs/ml312/lib/python3.12/site-packages/anthropic/_client.py:189, in Anthropic._validate_headers(self, headers, custom_headers)
        186 if isinstance(custom_headers.get("Authorization"), Omit):
        187     return
    --> 189 raise TypeError(
        190     '"Could not resolve authentication method. Expected either api_key or auth_token to be set. Or for one of the `X-Api-Key` or `Authorization` headers to be explicitly omitted"'
        191 )


    TypeError: "Could not resolve authentication method. Expected either api_key or auth_token to be set. Or for one of the `X-Api-Key` or `Authorization` headers to be explicitly omitted"



```python

```


```python

```


```python

```


```python

```


```python

```


---
**Score: 15**