import math
import string
import pandas as pd
from collections import Counter

data = pd.read_csv("address.csv")
parameters = data.columns
smlrty_list = []

for param in parameters:
    data[param] = data[param].str.lower()
    data[param] = data[param].astype(str).str.replace('no','', regex=True)
    data[param] = data[param].astype(str).str.replace(':','', regex=True)
    data[param] = data[param].astype(str).str.replace('.','', regex=True)
    data[param] = data[param].astype(str).str.replace('yolu','', regex=True)
    data[param] = data[param].astype(str).str.replace('mahallesi','', regex=True)
    data[param] = data[param].astype(str).str.replace('mah','', regex=True)
    data[param] = data[param].astype(str).str.replace('caddesi','', regex=True)
    data[param] = data[param].astype(str).str.replace('cad','', regex=True)
    data[param] = data[param].astype(str).str.replace('cd','', regex=True)
    data[param] = data[param].astype(str).str.replace('sokak','', regex=True)
    data[param] = data[param].astype(str).str.replace('sk','', regex=True)
    data[param] = data[param].astype(str).str.translate({ord(c): None for c in string.whitespace})

# Cosine similarity method
def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

# Implement similarity func to data
for x, y in zip(data['IS_ADRESI'], data['EV_ADRESI']):
    iş_adresi_C = Counter(x)
    ev_adresi_C = Counter(y)

    similarity = counter_cosine_similarity(ev_adresi_C, iş_adresi_C)
    smlrty_list.append(similarity)

data['SIMILARITY %'] = smlrty_list
print(data)