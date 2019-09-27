import json
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

def es_search(**kwargs):
    result = dict()
    result_set = list()
    search_terms = list()
    for key, value in kwargs.items():
        search_terms.append({"match": {key: value}})
 
    print(search_terms)
    size = es.count(index="truecrime").get("count")
    res = es.search(index="truecrime", size=size, body=json.dumps({"query": {"bool": {"must": search_terms}}}))
    for hit in res["hits"]["hits"]:
        result.update({"total": res["hits"]["total"], \
                        "source": hit["_source"]["source"], \
                        "subject": hit["_source"]["subject"], \
                        "story": hit["_source"]["story"]})
        if "quote" in hit["_source"]:
            result.update({"quote": hit["_source"]["quote"]})
        result_set.append(result)
    return result_set

#print(es_search(story="name"))
