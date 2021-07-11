import pandas as pd
abs_file = '/Users/whkoh/PycharmProjects/preppin-data/2021-wk24/Absenteeism Scaffold.xlsx'

absence_df = pd.read_excel(abs_file, sheet_name='Reasons')
out_df = pd.DataFrame(columns=['Name', 'Days_Absence'])
# print(f'first out_df is {out_df}')
for i in range(len(absence_df)):
    # count_absence = absence_df.iloc[i]['Days Off']
    for j in range(absence_df.iloc[i]['Days Off']):
        # jrow = pd.DataFrame()
        # jrow['Name'] = absence_df.iloc[i]['Name']
        # jrow['Days_Absence'] = absence_df.iloc[i]['Start Date'] + pd.Timedelta(days=j)
        jrow = [absence_df.iloc[i]['Name'], absence_df.iloc[i]['Start Date'] + pd.Timedelta(days=j)]
        out_df.loc[len(out_df)] = jrow
        # print(out_df)
    # out_df =
print('')