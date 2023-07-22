# sentence-tokens-embeddings
exploring embeddings approaches with tokens, sentences and in between combinations

## notebook

[sentence-transformers.ipynb](sentence-transformers.ipynb)

## sentence transformers
https://github.com/UKPLab/sentence-transformers

## openai
```python
response = openai.Embedding.create(
    input=text_input,
    model="text-embedding-ada-002",
    user="openai_faiss.py"
)
```
* example from vectorMind [openai-faiss](https://github.com/VectorMind/openai-faiss/blob/a6600bcd58940d5ec3f008b0e3299265144b5ded/openai_faiss.py#L25)

