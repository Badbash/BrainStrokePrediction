import pandas as pd
import numpy as np
df=pd.read_csv('/Users/sumlipuri/Desktop/Brainstorm-Final/df.csv')
x = ['age' , 'gender' , 'bmi' , 'heart_disease' , 'hypertension' , 'avg_glucose_level' , 'smoking_status']
y = ['stroke']
t_x = df[x]
t_y = df['stroke']
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
def check_brainstroke(a,b,c,d,e,f,g):
    from sklearn.model_selection import train_test_split
    x_train , x_test , y_train , y_test = train_test_split(t_x,t_y , train_size=0.9)
    from sklearn.metrics import accuracy_score
    model = Pipeline([
                      ('scalar',MinMaxScaler()),
                      ('RandomForestClassifier', RandomForestClassifier())])

    model.fit(x_train,y_train)
    pred = model.predict(x_test)

    acc = accuracy_score(pred , y_test)
    lst = [[a,b,c,d,e,f,g]]
    pred1 = model.predict(lst)
    if pred1 == 0:
        return ("The patient is safe and accuracy is", acc*100 ,"%")
    else:
        return ("The patient may suffer from brainstroke and accuracy is" ,acc*100,"%")
    

 