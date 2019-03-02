import pandas as pd 
from sklearn import linear_model
dataset = pd.read_csv('weatherHistory.csv')
X=dataset.drop(['Daily Summary','Precip Type','Visibility (km)'],axis=1)
X = pd.get_dummies(X, columns=["Summary"])
Y=dataset[['Visibility (km)']]
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
#predicting the values
y_pred=regr.predict(X)
#Evaluating the model

from sklearn.metrics import mean_squared_error, r2_score
print("Variance score: %.2f" % r2_score(Y,y_pred))
print("Mean squared error: %.2f" % mean_squared_error(Y,y_pred))