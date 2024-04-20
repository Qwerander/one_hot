import random
import pandas as pd

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

one_hot_df = pd.DataFrame(0, columns=unique_values, index=data.index)

for index, value in data['whoAmI'].items():
    one_hot_df.loc[index, value] = 1

data_one_hot = pd.concat([data, one_hot_df], axis=1)

data_one_hot.drop(columns=['whoAmI'], inplace=True)

result = data_one_hot.head(n=10)

print(result)
