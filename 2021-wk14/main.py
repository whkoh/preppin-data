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
print('ok')