import ir_datasets
import gzip


DATASETS = ['msmarco-passage/trec-dl-2019/judged', 'msmarco-passage/trec-dl-2020/judged']

for ds_id in DATASETS.keys():
    target_file = ds_id.replace('/', '-') + '.jsonl.gz'
    dataset = ir_datasets.load(ds_id)
    queries = {}
    for query in dataset.queries_iter():
        queries[query.query_id] = query.default_text()
    
    docs = dataset.docs_store()

    #with gzip.open()
    for qrel in dataset.qrels_iter():
        print({"query_id": qrel.query_id, "doc_id": qrel.doc_id, "query": queries[qrel.query_id], "text": docs[qrel.doc_id]})
        break

