import re
import pandas as pd

no_dict = {
    "322": "Adana",
    "416": "Adıyaman",
    "312": "Ankara",
    "216": "İstanbul (Anadolu Yakası)",
    "212": "İstanbul (Avrupa Yakası)",
    # .
    # .
    # .
}

data = pd.read_csv("tel_no.csv")
organized_phone_numbers = []

for no in data['TELEFON']:
    no = no.replace(' ', '')
    if no.startswith("+90") or no.startswith("0"):
        no = no.replace("+90", "")
        no = no.replace("0", "", 1) # 1 : is count how many times you wanna relace the chars
        organized_phone_numbers.append(no)
    else:
        organized_phone_numbers.append(no)

data['TELEFON'] = organized_phone_numbers
data['NUMBER_TYPE'] = None

index_phone = data.columns.get_loc('TELEFON')
index_type = data.columns.get_loc('NUMBER_TYPE')
len_pattern = r'([0-9]{10})'
p_type_pattern = '(^5)'
first_3_char_pattern = r'([0-9]{3})'

for row in range(0, len(data)):

    lenn = re.search(len_pattern, data.iat[row, index_phone])
    type = re.search(p_type_pattern, data.iat[row, index_phone])
    p_city = re.search(first_3_char_pattern, data.iat[row, index_phone])

    if bool(lenn) == True and bool(type) == True:
        lenn = lenn.group()
        data.iat[row, index_type] = 'PHONE'

    elif bool(lenn) == True and bool(type) == False:
        lenn = lenn.group()

        if bool(p_city) == True:
            p_city = p_city.group()

            for k in no_dict.keys():
                if k == p_city:
                    data.iat[row, index_type] = no_dict[k] + ', SABIT'
    else:
        data.iat[row, index_type] = 'CITY CODE UNKNOWN NOT A PHONE CAN BE SABIT'

data['NUMBER_TYPE'] = data['NUMBER_TYPE'].astype(str).str.replace('None','CITY CODE NOT IN THE LIST', regex=True)

data.to_csv('categorized_phone_nums.csv', index=False)

# https://www.alomaliye.com/alan-kodlari/