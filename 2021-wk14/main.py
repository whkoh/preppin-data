import pandas as pd

passengers_df = pd.read_excel('Week 14 - Input.xlsx', sheet_name='Passenger List')
seatsloc_df = pd.read_excel('Week 14 - Input.xlsx', sheet_name='SeatList')
flights_df = pd.read_excel('Week 14 - Input.xlsx', sheet_name='FlightDetails')
planedetails_df = pd.read_excel('Week 14 - Input.xlsx', sheet_name='PlaneDetails')

flights_df[['FlightID', 'Dep_Airport', 'Arr_Airport', 'Dep_Date',
            'Dep_Time']] = flights_df.iloc[:,0].str.split('|', expand=True)
flights_df.drop(flights_df.columns[0], axis=1, inplace=True)
flights_df.iloc[:, 0] = flights_df.iloc[:, 0].str[1:3]
flights_df.iloc[:, 4] = flights_df.iloc[:, 4].str[0:8]

labelseat_dict = [['A', 'Window'], ['F', 'Window'], ['B', 'Middle'], ['E', 'Middle'], ['C', 'Aisle'],
                  ['D', 'Aisle']]
labelseat_df = pd.DataFrame(labelseat_dict, columns=['RowCol', 'SeatLabel'])

seatsloc_df = pd.melt(seatsloc_df, id_vars=['Row'], var_name='RowCol')
# seatsloc_df['SeatConc'] = seatsloc_df.agg(lambda x: f"{x['RowCol']}{x['value']}", axis=1)
seatsloc_df.rename(columns={'value': 'SeatNumber'}, inplace=True)
seatsloc_df = seatsloc_df.merge(labelseat_df, on='RowCol', how='outer')

print('ok')