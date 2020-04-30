import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
#from skelarn.externals import joblib
import pickle

data_file = open("boston_housing.pkl", "ab")

boston = load_boston()
print boston.keys()
print boston.feature_names
print boston.target
x = pd.DataFrame(boston.data, columns = boston.feature_names)
y = boston.target
print x.head()
print type(x)
print type(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.2, random_state = 1)

model = LinearRegression(fit_intercept = True, normalize = True, n_jobs = -1)
model.fit(x_train, y_train)

predict = model.predict(x_test)

#joblib.dump(model, 'boston_housing.pkl')
pickle.dump(model, data_file)

#model = joblib.load('boston_housing.pkl')
#model = pickle.load(data_file)
print model.coef_
print (np.sqrt(mean_squared_error(y_test, predict)))

print r2_score(y_test, predict)

data_file.close()
print model.rank_
print model.singular_
print model.coef_


