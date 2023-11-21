import pandas as pd
import numpy as np
# 整形变量
year0 = 1990
year1 = 2023
years = list(range(year0, year1))  #years 序列变量
years = np.array(years) # np.array)
builtupArea = years * 0.319 + np.random.randint(-100, 100) * 0.045
# dictionary 映射/字典类型
data = {
"year": years,
 "builtupArea": builtupArea
}
pdf = pd.DataFrame(data = data)
pdf.to_csv('builtupArea-蔡权.csv', index=False)