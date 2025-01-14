

Run tests via:

```
PYTHONPATH=src pytest
```


```
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm LiteLLM --model llama3.1
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm LiteLLM --model llama3
OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm OpenAiGPT --model gpt-4o-mini
python3 src/predict.py --prompt umbrella_zeroshot_basic --llm OpenAiGPT --model gpt-4o
python3 src/predict.py --prompt umbrella_zeroshot_basic --llm GeminiGPT --model gemini-1.5-flash
python3 src/predict.py --prompt umbrella_zeroshot_basic --llm GeminiGPT --model gemini-1.5-flash-8b


ANTHROPIC_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm AnthropicLLM --model claude-3-sonnet-20240229
ANTHROPIC_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm AnthropicLLM --model claude-3-haiku-20240307
ANTHROPIC_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm AnthropicLLM --model claude-3-5-sonnet-20241022
ANTHROPIC_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm AnthropicLLM --model claude-3-5-haiku-20241022

OPENAI_API_KEY= python3 src/predict.py --prompt umbrella_zeroshot_basic --llm GroqLLM --model mixtral-8x7b-32768

```
TODO: Add groq
2*anthropic

mixtral


unsloth

