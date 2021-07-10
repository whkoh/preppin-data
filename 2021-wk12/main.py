import pandas as pd
import numpy as np

def main():
    indf = pd.read_csv('Tourism Input.csv')
    in2df = pd.melt(indf, id_vars=indf.columns[0:3], var_name='yr_mo', value_name='measure', value_vars=indf.columns[4:])
    in2df.dropna(inplace=True)
    in2df = in2df[in2df['Hierarchy-Breakdown'].str.slice(0,40) == 'Real Sector / Tourism / Tourist arrivals']
    in2df['type'] = np.where(in2df['Hierarchy-Breakdown'] == 'Real Sector / Tourism / Tourist arrivals',
                             'continent', 'country')  # Split workflow to country and continent
    in2df['Country'] = np.where(in2df['Series-Measure'].str.contains('from'),
                                in2df['Series-Measure'].str.slice(22,len(in2df['Series-Measure'])),
                                'UN and others')
    in2df.loc[in2df['measure'] == 'na', 'measure'] = 0
    countrydf = in2df[in2df['type'] == 'country']
    continentdf = in2df[in2df['type'] == 'continent']
    countrydf['Breakdown'] = countrydf['Hierarchy-Breakdown'].str.slice(43,len(countrydf['Hierarchy-Breakdown']))


    print('test')

if __name__ == '__main__':
    main()
