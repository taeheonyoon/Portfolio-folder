import pickle
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

dataset = pd.read_csv('titanic/ml/ml_model.py', encoding='utf-8')
dataset = dataset.rename(colums=lambda x: x.strip().lower())
dataset.head()

dataset = dataset[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'survived']]
dataset['sex'] = dataset['sex'].map({'male': 0, 'female': 1})
dataset['age'] = pd.to_numeric(dataset['age'], errors='coerce')
dataset['age'] = dataset['age'].fillna(np.mean(dataset['age']))

embarked_dummies = pd.get_dummies(dataset['embarked'])
dataset = pd.concat([dataset, embarked_dummies], axis=1)
dataset = dataset.drop(['embarked'], axis=1)

X = dataset.drop(['survived'], axis=1)
Y = dataset['survived']

sc = MinMaxScaler(feature_range=(0, 1))
X_scaled = sc.fit_transform(X)

pickle.dump(log_model, open("ml_model.sav", "wb"))
pickle.dump(sc, open("scaler.sav", "wb"))