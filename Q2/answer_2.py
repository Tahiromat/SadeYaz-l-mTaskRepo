import os
import pandas as pd

data = pd.read_csv("mail.csv")
mails = data.EMAIL

names_list = []
companies_list = []

for mail in mails:
    mail = mail.lower()
    mail = mail.replace('.com', "")
    mail = mail.replace('.tr', "")
    splt_m = mail.split("@")

    if splt_m[1] == "gmail":
        splt_m[1] = "unknown"

    names_list.append(splt_m[0])
    companies_list.append(splt_m[1])

df = pd.DataFrame()
df['NAMES'] = names_list
df['COMPANIES'] = companies_list

print(df)

uniq_companies_list = df['COMPANIES'].unique()

for c in uniq_companies_list:
    df_n = df.where(df['COMPANIES'] == c)
    df_n = df_n.dropna(how='all')
    df_n.to_csv("/home/tahir/Documents/DataScience/SadeYazılımTask/Q2/" + c + ".csv")