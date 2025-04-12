
# LLM Find My Fund 

Most FinTech platforms today manage massive datasets of Stocks, Mutual funds, ETFs, and other securities — especially in the Indian market.

 Yet, their search capabilities are limited, often relying on databases of fuzzy string match systems. These traditional methods struggle with incomplete inputs, typos, and ambiguous queries.

So we built a compact, intelligent language model that accurately matches a user’s query to the right mutual fund or security — even with fuzzy, partial, or unclear inputs.




### SLM Model: MiniLM L6 v2

This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.

It is a pretrained and finetuned model that we have utilized in our project.


MiniLM is based on the Transformer architecture, the same architecture used in models like BERT, RoBERTa, and GPT.
It uses self-attention mechanisms to process input text and create contextualized embeddings for tokens.


The L6 in the name indicates that the model has 6 Transformer layers (or encoder layers).
This is significantly smaller compared to BERT-base (12 layers) or BERT-large (24 layers), making it more lightweight and faster for inference.


### Metadata Referenced For Search Querying

- name
- shortName
- securityType
- assetAllocation
- sector


## Evaluation Metrics

We list the the first 5 most relevant matches to the user inputted string and display it along with match accuracy to show the accuracy of our search result. We have also modeled our project to accept queries and give the relevant fund/company in response

## Deployment

To deploy this project as an APK run

```bash
  flet build apk --module-name app
```

To deploy this project as a windows app

```bash
  flet build windows --module-name app
```

To run deploy project as a Linux app

```bash
  flet build linux --module-name app
```

Else this project can be ran out of your compiler or locally using 

```bash
flet run [script]
```

## Authors

- [@Calvin](https://github.com/Calvyin)
- [@Radian](https://github.com/Radian1308)
- [@Ishita](https://github.com/ishitasampat)
- [@DamnOctopus](https://github.com/damnoctopus)
