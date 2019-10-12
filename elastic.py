import json
from elasticsearch import Elasticsearch
es = Elasticsearch()


def es_insert(category, source, subject, story, **extras):
    doc = {
        "source": source,
        "subject": subject,
        "story": story,
        **extras,
    }
    res = es.index(index=category, doc_type="story", body=doc)
    print(res["result"])


def es_update(category, id, **extras):
    body = {"body": {"doc" : { **extras, } } }
    res = es.update(index=category, doc_type="story", id=id, body=body)
    print(res["result"])


def es_search(**filters): #added id
    result = dict()
    result_set = list()
    search_terms = list()
    for key, value in filters.items():
        search_terms.append({"match": {key: value}})
 
    print("Search terms:", search_terms)
    size = es.count(index="truecrime").get("count")
    res = es.search(index="truecrime", size=size, body=json.dumps({"query": {"bool": {"must": search_terms}}}))
    for hit in res["hits"]["hits"]:
        result = {"total": res["hits"]["total"], \
                        "id": hit["_id"], \
                        "source": hit["_source"]["source"], \
                        "subject": hit["_source"]["subject"], \
                        "story": hit["_source"]["story"]}
        if "quote" in hit["_source"]:
            result.update({"quote": hit["_source"]["quote"]})
        result_set.append(result)
    return result_set
