import re
import numpy as np
import pandas as pd

data = pd.read_csv("address.csv")
data['TC'] = None

index_address = data.columns.get_loc('ADDRESS')
index_tc = data.columns.get_loc('TC')
tc_pattern = r'([0-9]{11})'

for row in range(0, len(data)):
    tc = re.search(tc_pattern, data.iat[row, index_address])
    if bool(tc) == True:
        tc = tc.group()
        data.iat[row, index_tc] = tc
        data.iat[row, index_address] = data.iat[row, index_address].replace(tc, '')
    else:
        pass

data['TC'] = data['TC'].astype(str).str.replace('None','UNKNOWN', regex=True)
print(data)
