import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import accuracy_score as score
from sklearn.model_selection import train_test_split
data = pd.read_csv('D:\\all prOJECT\project sem 5\pract\data.csv' , names = ["10th" , "12th"  , "cgpa" , "automata" , "automata_fix" ,"computer sc","computer sc perc" , "writex" , "logitcal" ,  "logical perc" , "computer programming" , "computer programming perc" , "Quant" , "Quant perc" , "English" , "English Perc" , "total" , "y_label" ])
data["total"] = data["total"].astype(float)
data["y_label"][data.total > 4500] = 1
data["y_label"][data.total <= 4500] = 0
X_train , X_test , Y_train , Y_test =train_test_split(data.iloc[:,0:16] , data.iloc[:,17] , test_size = 0.2 , random_state = 1)
X_train , X_cv , Y_train , Y_cv = train_test_split(X_train ,Y_train , test_size = 0.2 , random_state = 1)
model = knn(n_neighbors = 75)
model.fit(X_train , Y_train)