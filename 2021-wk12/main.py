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
                                in2df['Series-Measure'].str.slice(22, len(in2df['Series-Measure'])),
                                'UN and others')
    in2df.loc[in2df['measure'] == 'na', 'measure'] = 0
    in2df['measure'] = in2df['measure'].astype(float)
    # print(in2df.dtypes)
    countrydf = in2df[in2df['type'] == 'country']  # Separately analyse country and continents
    continentdf = in2df[in2df['type'] == 'continent']
    continentdf.rename(columns={'Country': 'Breakdown'}, inplace=True)
    continentdf_grp = continentdf.groupby(['yr_mo', 'Breakdown']).sum()
    input_sum = continentdf_grp['measure'].sum()
    countrydf['Breakdown'] = countrydf['Hierarchy-Breakdown'].str.slice(43, len(countrydf['Hierarchy-Breakdown']))
    countrydf_grp = countrydf.groupby(['yr_mo', 'Breakdown']).sum()  # Use this to compare to continent
    detail_sum = countrydf_grp['measure'].sum()
    deltas_df = pd.merge(left=continentdf_grp, right=countrydf_grp, how='outer', on=['yr_mo', 'Breakdown'])
    deltas_df.fillna(0, inplace=True)
    deltas_df.drop(columns=['id_x', 'id_y'], inplace=True)
    deltas_df['delta'] = deltas_df['measure_x'] - deltas_df['measure_y']
    deltas_df['Country'] = 'Unknown'
    deltas_df = deltas_df[deltas_df['delta'] != 0]
    deltas_df.rename(columns={'delta': 'measure'}, inplace=True)
    deltas_df.drop(columns=['measure_x', 'measure_y'], inplace=True)
    deltas_df.set_index(['Country'], append=True, inplace=True)
    unknown_sum = deltas_df['measure'].sum()
    compute_sum = detail_sum + unknown_sum
    # print(f'input_sum --> {input_sum}')
    # print(f'sums --> {compute_sum}')
    assert input_sum == compute_sum, 'sums do not compute'  # if continent sum does not equal, we need to check
    countrydf_spc = countrydf.groupby(['yr_mo', 'Breakdown', 'Country']).sum()
    final_df = pd.concat([countrydf_spc, deltas_df])
    final_sum = final_df['measure'].sum()
    assert input_sum == final_sum, 'final sum does not compute'  # if continent sum does not equal, we need to check
    final_df.drop(['id'], axis=1, inplace=True)
    # print(final_df.head(20))

if __name__ == '__main__':
    main()
