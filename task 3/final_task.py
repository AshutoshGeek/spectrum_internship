import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics as m
from sklearn.metrics import r2_score as rrr
from sklearn.feature_selection import SelectKBest , chi2


df = pd.read_csv('student-math.csv', sep=';')
le = LabelEncoder()
lm=LinearRegression()

def yesno(x):
    if(x=='yes'):
        return 1
    elif(x=='no'):
        return 0
    

df['Total_grades'] = df['G1'] + df['G2'] + df['G3']
df.drop(['G3'], axis=1,inplace= True)



#print(df)
df['paid']=df['paid'].apply(yesno)
df['schoolsup']=df['schoolsup'].apply(yesno)
df['famsup']=df['famsup'].apply(yesno)
df['activities']=df['activities'].apply(yesno)
df['nursery']=df['nursery'].apply(yesno)
df['higher']=df['higher'].apply(yesno)
df['internet']=df['internet'].apply(yesno)
df['romantic']=df['romantic'].apply(yesno)

df['school'] = le.fit_transform(df['school'])
df['sex'] = le.fit_transform(df['sex'])
df['address'] = le.fit_transform(df['address'])
df['famsize'] = le.fit_transform(df['famsize'])
df['Pstatus'] = le.fit_transform(df['Pstatus'])

a1 = pd.get_dummies(df['reason'],drop_first=True)
a2 = pd.get_dummies(df['Mjob'],drop_first=True)
a3 = pd.get_dummies(df['Fjob'],drop_first=True)
a4 = pd.get_dummies(df['guardian'],drop_first=True)

#print(a1)
df.drop(['reason','Mjob','Fjob','guardian'],axis=1,inplace=True)

dff = pd.concat([df,a1,a2,a3,a4],axis=1)

x=dff.copy()
x.drop('Total_grades',axis=1,inplace=True)

y=df['Total_grades']
bestfeatures = SelectKBest(score_func=chi2,k=10)
fitt = bestfeatures.fit(x,y)

dfscores = pd.DataFrame(fitt.scores_)
dfcolumns = pd.DataFrame(x.columns)
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']
#print(featureScores.nlargest(30,'Score'))
#print(featureScores.nsmallest(20,'Score'))
sortdf=featureScores.nsmallest(34,'Score') 
#print(list(sortdf.Specs))

#x.drop(['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu','traveltime', 'studytime', 'schoolsup', 'famsup', 'paid','activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel','freetime', 'goout','Dalc', 'Walc', 'health','home', 'other', 'reputation', 'health', 'other', 'services', 'teacher','health', 'other', 'services', 'teacher', 'mother', 'other'],axis=1,inplace=True)
x.drop(list(sortdf.Specs),axis=1,inplace=True)
print("The best features to be considered are ",list(x.columns)) 

xtrain,xtest,ytrain,ytest= train_test_split(x,y,test_size=0.3,random_state=101)
lm.fit(xtrain,ytrain)
pdata = lm.predict(xtest)


print("RMSE = ",np.sqrt(m.mean_squared_error(ytest,pdata)))

score = rrr(ytest,pdata)*100
print("r2.score = ",score)


