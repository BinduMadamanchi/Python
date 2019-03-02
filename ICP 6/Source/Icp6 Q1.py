import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('train.csv')
print ("Train data shape:", train.shape)
#data = pd.concat([train['SalePrice'], train[var]], axis=1)
xData = train['GarageArea']
yData = train['SalePrice']

plt.xlabel('GarageArea Field')

plt.ylabel('SalePrice')
plt.scatter(xData, yData)
plt.show()

z = np.abs(stats.zscore(data))
print(z)
threshold=3
print(np.where(z>3))


Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


data = data[(z < 3).all(axis=1)]
data.shape


var ='GarageArea'
plt.scatter(x=data['GarageArea'], y=data['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground grade living area square feet')
plt.show()