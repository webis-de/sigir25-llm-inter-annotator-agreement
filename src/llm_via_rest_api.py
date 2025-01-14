class LLMForRelevanceJudgment:
    def generate(self, query : str, passage : str):
        """ Generate a response with a instruct LLM.

        Args:
            query (str): the query
            passage (str): the document

        Returns:
            str: LLM response
        """
        raise ValueError('ToDo: implement this method to generate response for {query} and {document}.')


class AnthropicLLM(LLMForRelevanceJudgment):
    def __init__(self, prompt: str, model : str) -> None:
        """_summary_

        Args:
            prompt (_type_): _description_
            model (_type_): _description_
            preamble (_type_, optional): _description_. Defaults to None.
        """
        import anthropic

        self._model = model
        self._client = anthropic.Anthropic()
        self._prompt = prompt
        self._preamble = None

    def generate(self, query : str, passage : str):
        """ Generate a response with a instruct LLM.

        Args:
            query (str): the query
            passage (str): the document

        Returns:
            str: LLM response
        """
        messages = []
        if self._preamble:
            messages.append(
                {
                    "role": "system",
                    "content": self._preamble
                }
            )
        
        formatted = self._prompt(query, passage)
        messages.append({
            "role": "user",
            "content": [{"type": "text", "text": formatted}]
        })

        output = self._client.messages.create(model=self._model, messages=messages, max_tokens=1000)

        return {"content": output.content[0].text, "role": "assistant"}

class OpenAiGPT(LLMForRelevanceJudgment):
    def __init__(self, prompt: str, model : str, preamble : str = None, **kwargs) -> None:
        """_summary_

        Args:
            prompt (_type_): _description_
            model (_type_): _description_
            preamble (_type_, optional): _description_. Defaults to None.
        """
        from openai import OpenAI as cli
        import tiktoken

        self._model = model # Model name
        self._client = cli() # OpenAI client
        self._prompt = prompt # Outlines prompt
        self._preamble = preamble # System prompt
        self._kwargs = kwargs # All completion parameters e.g max_tokens, temperature ...
        self._tokenizer = tiktoken.encoding_for_model(model) # Tokenizer (Needed to encode doc tokens)

    def generate(self, query : str, passage : str):
        """ Generate a response with a instruct LLM.

        Args:
            query (str): the query
            passage (str): the document

        Returns:
            str: LLM response
        """
        messages = []
        if self._preamble:
            messages.append(
                {
                    "role": "system",
                    "content": self._preamble
                }
            )
        
        formatted = self._prompt(query, passage)
        messages.append({
            "role": "user",
            "content": formatted
        })

        output = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            **self._kwargs
        )
        
        return output.choices[0].message.to_dict()

class GeminiGPT(OpenAiGPT):
    def __init__(self, prompt: str, model : str, preamble : str = None, **kwargs) -> None:
        """_summary_

        Args:
            prompt (_type_): _description_
            model (_type_): _description_
            preamble (_type_, optional): _description_. Defaults to None.
        """
        from openai import OpenAI as cli
        import tiktoken

        self._model = model # Model name
        self._client = cli(base_url="https://generativelanguage.googleapis.com/v1beta/openai/") # OpenAI client
        self._prompt = prompt # Outlines prompt
        self._preamble = preamble # System prompt
        self._kwargs = kwargs # All completion parameters e.g max_tokens, temperature ...

class LiteLLM(LLMForRelevanceJudgment):
    def __init__(self, prompt: str, model : str, preamble : str = None, **kwargs) -> None:
        """_summary_

        Args:       
            prompt (_type_): _description_
            model (_type_): _description_
            preamble (_type_, optional): _description_. Defaults to None.
        """
        from openai import OpenAI as cli
        import tiktoken

        self._model = model # Model name
        self._client = cli(base_url='https://llms-inference.innkube.fim.uni-passau.de') # OpenAI client
        self._prompt = prompt # Outlines prompt
        self._preamble = preamble # System prompt
        self._kwargs = kwargs # All completion parameters e.g max_tokens, temperature ...

    def generate(self, query : str, passage : str):
        """ Generate a response with a instruct LLM.

        Args:
            query (str): the query
            passage (str): the document

        Returns:
            str: LLM response
        """
        messages = []
        if self._preamble:
            messages.append(
                {
                    "role": "system",
                    "content": self._preamble
                }
            )
        
        formatted = self._prompt(query, passage)
        messages.append({
            "role": "user",
            "content": formatted
        })

        output = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            **self._kwargs
        )
        
        return output.choices[0].message.to_dict()  

__all__ = sorted(list(['OpenAiGPT', 'LiteLLM', 'GeminiGPT', 'AnthropicLLM']))