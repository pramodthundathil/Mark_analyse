import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("predict/predict1.csv")
print(data.head(10))
print(data.isnull().sum())
print(data["IQ"].value_counts())
# figure = px.scatter(data_frame=data, x = "number_courses", 
#                     y = "Marks", size = "time_study", 
#                     title="Number of Courses and Marks Scored")
# figure.show()

# figure = px.scatter(data_frame=data, x = "time_study", 
#                     y = "Marks", size = "number_courses", 
#                     title="Time Spent and Marks Scored", trendline="ols")
# figure.show()

# correlation = data.corr()
# print(correlation["CGPA"].sort_values(ascending=False))

x = np.array(data[["Time", "IQ","tenth","twelve","S1","S2","S3","S4"]])
y = np.array(data["CGPA"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)

model = LinearRegression()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)
# features = np.array([[10, 7,97,99,9.2,8.2,8.6,7.4]])
# print(model.predict(features))

# data = pd.read_csv("predict/Student_Marks.csv")
# print(data.head(10))
# print(data.isnull().sum())
# print(data["number_courses"].value_counts())
# figure = px.scatter(data_frame=data, x = "number_courses", 
#                     y = "Marks", size = "time_study", 
#                     title="Number of Courses and Marks Scored")
# figure.show()

# figure = px.scatter(data_frame=data, x = "time_study", 
#                     y = "Marks", size = "number_courses", 
#                     title="Time Spent and Marks Scored", trendline="ols")
# figure.show()

# correlation = data.corr()
# print(correlation["Marks"].sort_values(ascending=False))

# x = np.array(data[["time_study", "number_courses"]])
# y = np.array(data["Marks"])
# xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
#                                                 test_size=0.2, 
#                                                 random_state=42)

# model = LinearRegression()
# model.fit(xtrain, ytrain)
# model.score(xtest, ytest)

# features = np.array([[12, 9]])
# print(model.predict(features))

def PredictionKNN():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import LabelEncoder

    sns.set_style('darkgrid')

    df = pd.read_csv("predict/exams.csv")
    print(df.head())

    df.describe()

    df["mean score"] = (df['math score'] + df["reading score"] + df ["writing score"])/3
    print(df.head())

    df['gender'].value_counts()

    lc = LabelEncoder()
    df['gender'] = lc.fit_transform(df['gender'])
    df['race/ethnicity'] = lc.fit_transform(df['race/ethnicity'])
    df['parental level of education'] = lc.fit_transform(df['parental level of education'])
    df['lunch'] = lc.fit_transform(df['lunch'])
    df['test preparation course'] = lc.fit_transform(df['test preparation course'])
    df.head()
    print(df.head())

    # sns.countplot(df['gender'], hue = df['race/ethnicity'])

    labels = ['None', 'Completed']
    colors = ['red', 'green']
    plt.pie(df['test preparation course'].value_counts() , labels = labels, colors = colors)
    # plt.show()

    plt.figure(figsize = (12,6))
    sns.barplot(x = 'test preparation course', y = 'mean score', data = df)

    sns.barplot(x = df['lunch'], y = df['mean score'], palette = 'inferno')

    sns.barplot(x = 'parental level of education', y = 'mean score', data = df)
    # plt.show()

    plt.figure(figsize = (12,6))
    sns.pairplot(df)
    plt.show()

    plt.figure(figsize = (12,6))
    sns.pairplot(df)
    plt.show()

    df = df.drop(['math score', 'writing score', 'reading score'],axis = 1)
    df.head()

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import classification_report, confusion_matrix
    y = df['mean score']
    x = df.drop(['mean score'], axis  = 1)
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)

    model = LogisticRegression(solver='liblinear', random_state=0)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    difference = abs(predictions - y_test)
    print(difference.mean())
# PredictionKNN()
