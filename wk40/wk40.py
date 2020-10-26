import pandas as pd

#%%
df = pd.DataFrame(columns=['name', 'count_name', 'gender', 'month'])


def wrapper(func, file, skip, nrow, usecolumn, gender, month):
    func(file, skip, nrow, usecolumn, gender, month)


def func(datafr, file, skip, nrow, usecolumn, gender, month):
    '''
    :param datafr: Pass in a dataframe to be appended.
    :param file: Which excel file to read
    :param skip: How many lines to skip for this part
    :param nrow: How many rows to read
    :param usecolumn: Which cols to read
    :param gender: Which gender (manual)
    :param month: Which month (manual)
    :return:
    '''
    df_temp = pd.read_excel(file, index_col=None, skiprows=skip, nrows=nrow, usecols=usecolumn, header=None, names=['name', 'count_name'])
    df_temp['gender'] = gender
    df_temp['month'] = month
    datafr = datafr.append(df_temp).reset_index(drop=True)
    return datafr

# pd_temp = pd.DataFrame(columns=['name', 'count_name', 'gender', 'month'])
#
# pd_temp = pd.read_excel('2019boysnames.xlsx', names=['name', 'count_name'], skiprows=7, nrows=10, usecols='B:C', header=None)
# pd_temp['gender'] = 'Male'
# pd_temp['month'] = 'January'


df = func(datafr=df, file='2019boysnames.xlsx', skip=7, nrow=10, usecolumn='B:C', gender='Male', month=1)
df = func(datafr=df, file='2019boysnames.xlsx', skip=7, nrow=10, usecolumn='F:G', gender='Male', month=2)
df = func(datafr=df, file='2019boysnames.xlsx', skip=7, nrow=10, usecolumn='J:K', gender='Male', month=3)
df = func(datafr=df, file='2019boysnames.xlsx', skip=7, nrow=10, usecolumn='N:O', gender='Male', month=4)
df = func(datafr=df, file='2019boysnames.xlsx', skip=21, nrow=10, usecolumn='B:C', gender='Male', month=5)
df = func(datafr=df, file='2019boysnames.xlsx', skip=21, nrow=10, usecolumn='F:G', gender='Male', month=6)
df = func(datafr=df, file='2019boysnames.xlsx', skip=21, nrow=10, usecolumn='J:K', gender='Male', month=7)
df = func(datafr=df, file='2019boysnames.xlsx', skip=21, nrow=10, usecolumn='N:O', gender='Male', month=8)
df = func(datafr=df, file='2019boysnames.xlsx', skip=35, nrow=10, usecolumn='B:C', gender='Male', month=9)
df = func(datafr=df, file='2019boysnames.xlsx', skip=35, nrow=10, usecolumn='F:G', gender='Male', month=10)
df = func(datafr=df, file='2019boysnames.xlsx', skip=35, nrow=10, usecolumn='J:K', gender='Male', month=11)
df = func(datafr=df, file='2019boysnames.xlsx', skip=35, nrow=10, usecolumn='N:O', gender='Male', month=12)

df = func(datafr=df, file='2019girlsnames.xlsx', skip=7, nrow=10, usecolumn='B:C', gender='Female', month=1)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=7, nrow=10, usecolumn='F:G', gender='Female', month=2)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=7, nrow=10, usecolumn='J:K', gender='Female', month=3)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=7, nrow=10, usecolumn='N:O', gender='Female', month=4)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=21, nrow=11, usecolumn='B:C', gender='Female', month=5)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=21, nrow=10, usecolumn='F:G', gender='Female', month=6)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=21, nrow=10, usecolumn='J:K', gender='Female', month=7)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=21, nrow=11, usecolumn='N:O', gender='Female', month=8)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=36, nrow=10, usecolumn='B:C', gender='Female', month=9)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=36, nrow=10, usecolumn='F:G', gender='Female', month=10)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=36, nrow=10, usecolumn='J:K', gender='Female', month=11)
df = func(datafr=df, file='2019girlsnames.xlsx', skip=36, nrow=12, usecolumn='N:O', gender='Female', month=12)

df['count_name'] = df['count_name'].astype(int)

df_rank = df.groupby(['gender', 'name']).sum()
df_rank = df_rank.reset_index()
df_rank['2019_rank'] = df_rank.groupby(['gender'])['count_name'].rank('dense', ascending=False)
df_rank.sort_values(by=['gender', '2019_rank'], ascending=[True, True], inplace=True)

