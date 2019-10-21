import re
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'modules')))
from elastic import es_search, es_update
from extract import get_arrest_date


for val in es_search():
    arrests = list()
    for result in re.finditer(r'(\w+\W+){0}(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(\w+\W+)\d{1,4},?\s\d{0,4}(\w+\W+){1,10}(captured|caught|seized|arrested|apprehended)', val.get("story"), flags=re.I):
        words = result.group().replace(",", "").split()
        arrest_date = words[:(3 if words[2].isdigit() == True else 2)]
        arrests.append(get_arrest_date(arrest_date))
 
    for result in re.finditer(r'(\w+\W+){0}(captured|caught|seized|arrested|apprehended)\s(\w+\W+){1,10}(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(\w+\W+)\d{1,4},?\s\d{0,4}', val.get("story"), flags=re.I):
        words = result.group().replace(",", "").split()
        arrest_date = words[(-3 if words[-2].isdigit() == True else -2):]
        arrests.append(get_arrest_date(arrest_date))

    if len(arrests) > 0:
        print(val.get("subject"), arrests)
        es_update("truecrime", val.get("id"), arrests=arrests)
