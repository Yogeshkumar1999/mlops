from sklearn.linear_model import LinearRegression
import pandas
data = pandas.read_csv("ml.csv")
print data.columns

X = data['duration'].values.reshape(5,1)
y = data['marks']
print y.shape
print type(y)
model = LinearRegression()
model.fit(X, y)
print model.predict([[6]])
