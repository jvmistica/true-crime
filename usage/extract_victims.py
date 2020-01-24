import os
import re
import sys
import spacy
sys.path.append(os.path.abspath(os.path.join('..', 'modules')))
from elastic import es_search, es_update
nlp = spacy.load("en_core_web_sm")


for val in es_search():
    victims = list()
    for result in re.finditer(r'(\w+\W+){0}victims?\s?(,|is|are|was|were)\s(\w+\W+){1,6}', \
                                val.get("story"), flags=re.I):
        doc = nlp(result.group())
        for entity in doc.ents:
            if entity.label_ == "PERSON":
                result_split = result.group().split()
                if "\n" in result.group():
                    pass
                elif "." in result.group():
                    period = result_split.index([i for i in result_split if "." in i][0])
                    if entity.text in result_split[period:]:
                        pass
                    else:
                        victims.append(entity.text)
                else:
                    victims.append(entity.text)

    if len(victims) > 0:
        print(val.get("subject"), victims)
        es_update("truecrime", val.get("id"), victims=victims)
