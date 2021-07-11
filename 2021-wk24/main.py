import pandas as pd
abs_file = '/Users/whkoh/PycharmProjects/preppin-data/2021-wk24/Absenteeism Scaffold.xlsx'

absence_df = pd.read_excel(abs_file, sheet_name='Reasons')
out_df = pd.DataFrame(columns=['Name', 'Days_Absence'])

for i in range(len(absence_df)):
    for j in range(absence_df.iloc[i]['Days Off']):
        jrow = [absence_df.iloc[i]['Name'], absence_df.iloc[i]['Start Date'] + pd.Timedelta(days=j)]
        out_df.loc[len(out_df)] = jrow

days_out_df = out_df.groupby(['Days_Absence']).count()
days_out_df.reset_index(inplace=True)

days_df = pd.DataFrame(columns=['Days_Absence'])
for i in pd.date_range(start='2021-04-01', end='2021-05-31'):
    days_df.loc[len(days_df)] = i

final_df = days_df.merge(days_out_df, how='left', on='Days_Absence')
final_df.fillna(0, inplace=True)