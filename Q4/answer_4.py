"""
Elimizde bazı okulların isimleri ve bulundukları mahallelerin olduğu bir liste mevcut.
Başka bir listede ise il, bu illerdeki ilçeler ve bu ilçelerdeki mahalleleri bulunduran
referans tablomuz var. Mahalle bilgisini ve bu referans tabloları kullanarak okulların
hangi il ve ilçede olduklarını nasıl bulursunuz?
"""

import pandas as pd

okul_mah_data = {
    "OKUL_ADI": ['Kavaklıdere İÖO', 'Etimesgut Anadolu Lisesi', 'Cumhuriyet Lisesi', 'Zafer İlkokulu'],
    "MAHALLE": ['Kavaklıdere', 'Eryaman', 'Bozkurt', 'Cumhuriyet']
}

il_data = {
    "IL": ['İSTANBUL','ANKARA', 'İZMİR','DENİZLİ']
}

il_ilce_data = {
    "IL": ['ANKARA','ANKARA', 'ANKARA','İSTANBUL'],
    "ILCE": ['ÇANKAYA','ALTINDAĞ', 'ETİMESGUT','ŞİŞLİ']

}

ilce_mah_data = {
    "ILCE": ['ÇANKAYA','ÇANKAYA', 'ÇANKAYA','ÇANKAYA','ŞİŞLİ', 'ŞİŞLİ','ŞİŞLİ'],
    "MAHALLE": ['KAVAKLIDERE','ESAT', 'AYRANCI','CUMHURİYET','BOZKURT', 'ESKİŞEHİR','CUMHURİYET']

}

okul_mah_table = pd.DataFrame(okul_mah_data, columns=['OKUL_ADI', 'MAHALLE'])
okul_mah_table.MAHALLE = okul_mah_table.MAHALLE.str.upper()
il_table = pd.DataFrame(il_data, columns=['IL'])
il_ilce_table = pd.DataFrame(il_ilce_data, columns=['IL', 'ILCE'])
ilce_mah_table = pd.DataFrame(ilce_mah_data, columns=['ILCE', 'MAHALLE'])

n = pd.merge(left = il_table, right = il_ilce_table, how='outer')

m = pd.merge(left = n, right = ilce_mah_table, how='inner')

p = pd.merge(left = m, right = okul_mah_table, how='outer', suffixes=('', '_drop')).filter(regex='^(?!.*_drop)')
print(p)

p.to_csv('school_city_data.csv', index=False)
