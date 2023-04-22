# Color Classifier Machine Learning Part
# Created by Konrad Ceglarski 2019
__author__ = "Konrad Ceglarski"

import pandas as pd
import numpy as np
import math
from sklearn import svm

data = pd.read_csv('example_colors.csv', sep=',', header=0)

x = np.array(data.drop(['name'], 1))
y = np.array(data['name'])

# print(data, '\n- end -\n', x, '\n- end -\n', y)

model = svm.SVC(probability=True)
model.fit(x, y)

def predict_color(r, g, b):
    colors = ['red', 'green', 'blue', 'orange', 'yellow', 'brown', 'purple', 'pink', 'cyan', 'gray', 'white', 'black']
    prediction = model.predict([[r, g, b]])
    probability = model.predict_proba([[r, g, b]])
    return colors.index(prediction), round(max(probability[0]) * 100, 2)