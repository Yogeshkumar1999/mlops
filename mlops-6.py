'''
import pandas as pd
dataset = pd.read_csv("ml.csv")
#print dataset
#corelation place main role in feature relation(-1,1)
print dataset['id']
print dataset.corr()#to get te corelation betwen the features
from sklearn.feature_selection import VarianceThreshold
#we have to give a threshold.
#s = VarianceThreshold(threshold = 0.0)
s = VarianceThreshold(threshold = 0.3)
s.fit(dataset)
print s.get_support()
#dataset.info
#dataset.head()
#dataset.columns
from sklearn.model_selection import train_test_split
#x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state = 0)
import matplotlib.pyplot as ply
import seaborn as sns
sns.fit()

plt.scatter(x_train, y_train)
plt.line(x_test, y_test)
'''
#coimputer vision
import cv2
cap = cv2.VideoCapture(0)
#stats, image = cap.read()# ti take picture

cap.release()



