import pandas as pd
df = pd.read_csv('50_Startups.csv')

print df.head()
print df.info()
print df.columns
x = df.iloc[:, :-1]
y = df['Profit']

print type(x)
print x.shape
print type(y)
print y.shape

print x.head()

x =  pd.get_dummies(x, drop_first = True)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
from sklearn.metrics import r2_score, mean_squared_error
print r2_score(y_test, y_predict)
print model.coef_
