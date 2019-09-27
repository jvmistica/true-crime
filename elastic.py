from elasticsearch import Elasticsearch
es = Elasticsearch()


def es_insert(category, source, subject, story, **kwargs):
    doc = {
        "source": source,
        "subject": subject,
        "story": story,
        **kwargs,
    }
    res = es.index(index=category, doc_type="story", body=doc)
    print(res["result"])

def es_query():
    res = es.search(index="truecrime", body={"query": {"match_all": {}}})
    print("Got Hits:", res['hits']['hits'])
    for hit in res['hits']['hits']:
        print(hit["_source"]["source"])
        print(hit["_source"]["subject"])
        print(hit["_source"]["story"])

es_query()
