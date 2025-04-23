## SIGIR 2025: Large Language Model Relevance Assessors Agree With One Another More Than With Human Assessors

This repository contains all code and predictions for the paper on "Large Language Model Relevance Assessors Agree With One Another More Than With Human Assessors" that is presented at SIGIR 2025.

# Motivation

Relevance judgments can differ across assessors but previous work has shown that such disagreements hardly impact effectiveness rankings of retrieval systems in case of differences between human assessors or in case of human vs.\ large language model (LLM) assessors. Still, so far, the agreement between different LLM assessors has not yet been studied on a larger scale. To close this gap, we compare eight LLM assessor models on three TREC retrieval scenarios (Deep Learning and RAG tracks) with each other and with human judgments. We find that the agreement between LLM assessors is higher than between LLMs and humans, and, importantly, that LLM assessors tend to favor retrieval systems that use LLMs in their ranking decisions: in our scenarios with 30-50 retrieval systems, the LLM assessor-based system rankings overestimate LLM-based re-rankers on average between 7 and 16 positions.


# Citation

`TBD.`

# Development

Please run all tests via:

```
PYTHONPATH=src pytest
```

# Do the inference

All predictions have been made via the following commands:

```
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm LiteLLM --model llama3.1
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm LiteLLM --model llama3
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm OpenAiGPT --model gpt-4o-mini
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm OpenAiGPT --model gpt-4o
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm GeminiGPT --model gemini-1.5-flash
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm GeminiGPT --model gemini-1.5-flash-8b
ANTHROPIC_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm AnthropicLLM --model claude-3-sonnet-20240229
ANTHROPIC_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm AnthropicLLM --model claude-3-haiku-20240307
```

