import pandas as pd

class DataInvestigator:
    def __init__(self, df):
        self.df = df

    def baseline(self, col):
        # col is a zero-indexed column number
        column_data = self.df.iloc[:, col] # iloc[row #, column #]
        return column_data.mode().iloc[0] # mode() returns the most frequent value

    def corr(self, col1, col2):
        correlation = self.df.iloc[:, col1].corr(self.df.iloc[:, col2])
        return correlation

    def zeroR(self, col):
         # col is a zero-indexed column number
        column_data = self.df.iloc[:, col] # iloc[row #, column #]
        return column_data.mode().iloc[0] # mode() returns the most frequent value


df = pd.read_csv('gallstone.csv')
di = DataInvestigator(df)
print(di.baseline(1))
print(di.corr(1, 2))
print(di.zeroR(1))


