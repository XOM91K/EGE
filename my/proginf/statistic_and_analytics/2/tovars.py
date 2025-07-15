import pandas as pd
import numpy as np
data = pd.read_excel('Online Retail.xlsx')
data = data.dropna()  # удаляем все строки, где есть пропущенные значения (например, не указан номер покупателя)
# {run: 'auto'}
cnt = 3  # @param {type: 'slider', min: 1, max: 20, step: 1}
print(data.head(cnt))