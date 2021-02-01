import pandas as pd

#读取
df = pd.read_csv()
df = pd.DataFrame(data=None, index=[], columns=[])
df = pd.Series([])

#排序
df.sort_values(by="键名")

#前
df.head()

#后
df.tail()

#切片与索引
df[:20]
df[:20]["label_name"]
#标签
df.loc["行", "列"]
df.loc[[], []]
#位置
df.iloc["行号", "列号"] = 30
