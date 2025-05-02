# import numpy as np
#
# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
# print(b)
#

import pandas as pd
# import matplotlib.pyplot as plt
# state_dict = {'North Carolina': 9535483,
#               'Virginia': 8001024,
#               'Tennessee': 6346105,
#               'South Carolina': 4625364,
#               'Georgia': 9687653}
# state_series = pd.Series(state_dict).astype(int)
#
# ax = state_series.plot(kind='bar', color='skyblue')  # Пример с столбчатой диаграммой
# plt.title('Население в штатах')# Добавляем заголовок
# plt.xlabel('Штат')             # Подпись оси X
# plt.ylabel('Население')        # Подпись оси Y
# plt.show()



# print(state_series)
# print(state_series.index)
# print(state_series.values)



tracks_df = pd.read_csv(r"tracks.csv",
                        encoding='cp1251',
                        sep=';',
                        index_col="ID")

print(tracks_df.iloc[2, 0])










