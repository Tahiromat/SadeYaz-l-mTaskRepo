
# data = {
#     "ID": ["1","2","3","4","5","6","7"],
#     "EMAIL": ["deniz@sadeyazilim.com", "kadir@SADEYAZILIM.COM", "kadir@afirma.com", "Ceyda@gmail.com", "ali@gmail.com", "tamer@sadeyazilim.com", "müge@testbank.com.tr"]
# }

# df = pd.DataFrame(data, columns=['ID', 'EMAIL'])
# df.to_csv("mail.csv", index=False)






# FOR Q7
# time conversion ----

# visualization ----
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data['Hour_Date'], y=data['PJM_Load_MW'], name="data"))
# # fig.add_trace(go.Line(x=valid.index, y=valid[forecast_parameter], name="validation"))
# fig.show()
    

# fig = px.line(x=data.index, y=data['PJM_Load_MW'])
# fig.add_trace(go.Box(x=data['Monthly_Date'], y=data['PJM_Load_MW'], name="data"))
# fig.show()




# data['Hour_Date'] = data['Datetime'].dt.hour
# data['Week_Date'] = data['Datetime'].dt.weekday
# data['Monthly_Date'] = data['Datetime'].dt.month
# new_df['Year_Date'] = new_df['Datetime'].dt.year


# new_df = new_df.loc[new_df['Datetime'] < '1999-01-01']











# data = {
#     "TCKN": ["71824829102","12381949284","71824829102","59382838321","71824829102"],
#     "AD": ["Ali","Ali","Ali","Ahmet","Mehmet"]
# }

# df = pd.DataFrame(data, columns=['TCKN', 'AD'])
# df.to_csv("tc_name_dublicates_data.csv", index=False)





# ##############################33




'''sns.pairplot(features_and_target.dropna(), hue='hour', x_vars=['hour','dayofweek', 'year','weekofyear'], y_vars='PJM_Load_MW', height=5, plot_kws={'alpha':0.15, 'linewidth':0})
plt.suptitle('Power Use MW by Hour, Day of Week, Year and Week of Year')
plt.show()'''



'''pjme_test.rename(columns={'PJM_Load_MW': 'TEST SET'}).join(pjme_train.rename(columns={'PJM_Load_MW': 'TRAINING SET'}), how='outer').plot(figsize=(15,5), title='PJM Load MW', style='.')
plt.show()'''


'''f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
fig = model.plot(pjme_test_fcst, ax=ax)
plt.show()'''

'''fig = model.plot_components(pjme_test_fcst)
fig.show()'''

'''f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
ax.scatter(pjme_test.index, pjme_test['PJM_Load_MW'], color='r')
fig = model.plot(pjme_test_fcst, ax=ax)
fig.savefig('pjme_test_fcst.png')
fig.show()'''


""" !!!!!
f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
ax.scatter(pjme_test.index, pjme_test['PJM_Load_MW'], color='r')
fig = model.plot(pjme_test_fcst, ax=ax)
ax.set_xbound(lower='2000-11-01', upper='2000-12-01')
ax.set_ylim(0, 60000)
plot = plt.suptitle('Forecast vs Actuals')
fig.savefig('sss.png')
plt.show()"""

""" !!!!!
f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
ax.scatter(pjme_test.index, pjme_test['PJM_Load_MW'], color='r')
fig = model.plot(pjme_test_fcst, ax=ax)
ax.set_xbound(lower='2000-12-01', upper='2000-12-08')
ax.set_ylim(0, 60000)
plot = plt.suptitle('First Week of Forecast vs Actuals')
plot.show()"""
