from elasticsearch import Elasticsearch
es = Elasticsearch()


def es_insert(category, source, subject, story):
    doc = {
        "source": source,
        "subject": subject,
        "story": story,
    }
    res = es.index(index=category, doc_type="story", body=doc)
    print(res["result"])
