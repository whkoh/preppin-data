import pandas as pd
abs_file = '/Users/whkoh/PycharmProjects/preppin-data/2021-wk24/Absenteeism Scaffold.xlsx'

absence_df = pd.read_excel(abs_file, sheet_name='Reasons')
out_df = pd.DataFrame(columns=['Name', 'DateAbs'])
for i in range(len(absence_df)):
    # count_absence = absence_df.iloc[i]['Days Off']
    for j in range(absence_df.iloc[i]['Days Off']):
        out_df.append(absence_df.iloc[i]['Name'], absence_df.iloc[i]['Start Date'] + pd.Timedelta(1, units='d'))
    # out_df =
print('')