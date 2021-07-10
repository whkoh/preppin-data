import pandas as pd

def main():
    indf = pd.read_csv('Tourism Input.csv')
    in2df = pd.melt(indf, id_vars=indf.columns[0:3], var_name='yr_mo', value_name='measure', value_vars=indf.columns[4:])
    print('test')

if __name__ == '__main__':
    main()
