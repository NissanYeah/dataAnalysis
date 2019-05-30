# Pandas

- 數據結構 
  - Series: 一維陣列，跟numpy的陣列不同的是，可以定義自己的index(任何資料型態)
  - DataFrame: 多個一維陣列。不同於Series只有index和values屬性，DataFrame還有columns屬性

### 基礎

- 引入Series, DataFrame函式

```py
import pandas as pd  # 引入 pandas 模組
from pandas import Series, DataFrame # 引入 pandas 模組中的 Series, DataFrame 函式
```


- 讀取xlsx檔案

```
$ python3 -m pip install xlrd 
```

### 資料

名字  | 中文  | 英語 | 數學 |
--------------|:-----:|-----:| ----:|
張飛  | 65 |  65 |  NaN | 
關羽  | 95 | 85 |  98 | 
趙雲  | 95 | 92 |  96 |
黃忠  | 80 | 88 |  77 |
典韋  | 80 | 90 |  90 |
典韋  | 80 | 90 |  90 |

```py
import pandas as pd  # 引入 pandas 模組
from pandas import Series, DataFrame # 引入 pandas 模組中的 Series, DataFrame 函式
score = DataFrame(pd.read_excel('exercise2.xlsx'))
```

- 刪除多餘的行數：drop_duplicates()

```py
data = data.drop_duplicates()
```

- 刪除指定的columns、row

```py
data = data.drop(columns=['數學'])
data = data.drop(index=['張飛'])
```
- 重新命名 columns

```py
data.rename(columns={'中文': 'chinese', '英語': 'english'}, inplace = True)

```

- 刪除空格 map(str.strip)
- 刪除左邊空格 map(str.lstrip)
- 刪除右邊空格 map(str.rstrip)
- 刪除特定符號 str.strip('符號')


```py
data = DataFrame({
  'name':[' 張飛 ',' 關羽 ','趙雲','黃忠'],
  'score':['$90','$20','$70','$30']
})
data['name']=data['name'].map(str.strip)
data['score']=data['score'].str.strip('$')
print(data)
```

- 轉換大小寫

``` py
# 全部大写
data.columns = data.columns.str.upper()
# 全部小写
data.columns = data.columns.str.lower()
# # 首字母大写
data.columns = data.columns.str.title()
```