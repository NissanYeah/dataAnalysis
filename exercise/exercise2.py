import pandas as pd
from pandas import Series, DataFrame
score = DataFrame(pd.read_excel('./exercise2.xlsx'))
score['英語']=score['英語'].str.strip('$')
score = score.drop_duplicates()
score['total']=score.sum(axis=1)


print(score)
