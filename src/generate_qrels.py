import re

import gzip
import json
import ir_datasets
from pathlib import Path

def parse_llm_response(response: str) -> int:
    "This method is from UMBRELA https://github.com/castorini/umbrela/blob/main/src/umbrela/utils/common_utils.py and will be properly cited in the paper."
    response = response.strip().lower()
    valid_res = 1
    answer = ""
    patterns = [
        r'"o"\s*[:-=]?\s*(0|1|2|3)',
        r"\'o\'\s*[:-=]?\s*(0|1|2|3)",
        r"o\s*[:-=]?\s*(0|1|2|3)",
        r'"overall_score"\s*[:-=]?\s*(0|1|2|3)',
        r'"overall"\s*[:-=]?\s*(0|1|2|3)',
        r'"overall score"\s*[:-=]?\s*(0|1|2|3)',
        r'"final score"\s*[:-=]?\s*(0|1|2|3)',
        r'final score\s*[:-=]?\s*(0|1|2|3)',
        r"final score is (0|1|2|3)",
        r'"final_score"\s*[:-=]?\s*(0|1|2|3)',
        r'"score"\s*[:-=]?\s*(0|1|2|3)',
        r'"o_score"\s*[:-=]?\s*(0|1|2|3)',
        r"output score is (0|1|2|3)",
        r"score is (0|1|2|3)",
        r"[a-zA-Z]+\s+is\s+(0|1|2|3)\s",
        r"relevance category\s*[:-=]?\s*(0|1|2|3)",
        r"relevance category\s*[:-=]?\s*(0|1|2|3)",
        r"relevance category is (0|1|2|3)",
        r"it falls into the category (0|1|2|3)",
        r"category\s*(0|1|2|3)",
        r"relevance category (0|1|2|3)",
        r"relevance category for this passage would be (0|1|2|3)",
        r"the relevance category would be (0|1|2|3)",
        r"\n*(0|1|2|3)",
    ]
    for pattern in patterns:
        matched = None
        for m in re.finditer(pattern, response, re.IGNORECASE | re.MULTILINE | re.DOTALL):
            matched = m

        if matched:
            answer = matched.group(1).capitalize()
            break
    if answer == "":
        answer = "0"
        valid_res = 0
        print(f"Invalid response: {response}")
    return int(answer), valid_res

LLMS = [
    'GeminiGPT-gemini-1.5-flash-8b',
    'GeminiGPT-gemini-1.5-flash',
    'OpenAiGPT-gpt-4o-mini',
    'OpenAiGPT-gpt-4o',
    'AnthropicLLM-claude-3-haiku-20240307',
    'AnthropicLLM-claude-3-5-haiku-20241022',
    'AnthropicLLM-claude-3-sonnet-20240229',
    'LiteLLM-llama3',
]

PROMPTS = [
    'umbrella_zeroshot_basic',
]

DATASETS = [
    'msmarco-passage-trec-dl-2019-judged','msmarco-passage-trec-dl-2020-judged', 'msmarco-passage-v2.1-trec-rag-2024-judged'
]

if __name__ == '__main__':
    for dataset in DATASETS:
        irds_id = dataset.replace('passage-', 'passage/').replace('-judged', '/judged')
        qrel_file = Path(f'data/{dataset}/qrels/trec.qrels.txt')
        if qrel_file.exists():
            continue

        qrels_iter = ir_datasets.load(irds_id).qrels_iter()

        with open(qrel_file, 'w') as f:
            for qrel in qrels_iter:
                f.write(f'{qrel.query_id} q0 {qrel.doc_id} {qrel.relevance}\n')

    for llm in LLMS:
        for prompt in PROMPTS:
            for dataset in DATASETS:
                qrels = []
                with gzip.open(f'data/{dataset}/predictions/{llm}-{prompt}.jsonl.gz') as f:
                    for l in f:
                        try:
                            l = json.loads(l)
                            qid, docno = l['query_id'], l['doc_id']
                            rel, val = parse_llm_response(l['prediction']['content'])
                            qrels.append(f'{qid} q0 {docno} {rel}')

                        except json.decoder.JSONDecodeError:
                            pass

                with open(f'data/{dataset}/qrels/{llm}-{prompt}.qrels.txt', 'w') as f:
                    for l in qrels:
                        f.write(l +'\n')
