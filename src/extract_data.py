import ir_datasets
from tqdm import tqdm
import gzip
import json


DATASETS = ['ir-lab-wise-2024/subsampled-ms-marco-rag-20250105-training', 'msmarco-passage/trec-dl-2019/judged', 'msmarco-passage/trec-dl-2020/judged']

for ds in DATASETS:
    target_file = ds.replace('/', '-') + '/inputs.jsonl.gz'
    dataset = ir_datasets.load(ds)
    queries = {}
    for query in dataset.queries_iter():
        queries[query.query_id] = query.default_text()
    
    docs = dataset.docs_store()

    with gzip.open(f'data/{target_file}', 'wt') as f:
        for qrel in tqdm(dataset.qrels_iter()):
            entry = {"query_id": qrel.query_id, "doc_id": qrel.doc_id, "query": queries[qrel.query_id], "text": docs.get(qrel.doc_id).default_text()}
            f.write(json.dumps(entry) + '\n')

