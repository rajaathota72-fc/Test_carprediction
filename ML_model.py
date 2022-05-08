import pandas as pd
import math
#import pandas_profiling as pp
df = pd.read_csv("car data.csv")
print(df.info())
#profile = pp.ProfileReport(df)
#profile.to_file("Report.html")
df_summary = df.describe(include="all")
#df_summary.to_csv("Summary.csv")
df_model = df.drop(["Car_Name"],axis=1)
df_model_all_dummies = pd.get_dummies(df_model)
df_model_all_dummies.to_csv("Cardata_1.csv")
y = df_model_all_dummies[["Selling_Price"]]
X = df_model_all_dummies.drop(["Selling_Price"],axis=1)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,shuffle=False,random_state=False)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)
print(model.coef_,model.intercept_)
y_pred = model.predict(X_test)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,y_pred)
rmse = math.sqrt(mse)
print(rmse)
"""
newvalues = [[2019,700000,40000,1,0,0,1,0,1,1,0]]
predicted_price = model.predict(newvalues)
print(predicted_price)
"""
## pickling - serialisation
import pickle
f = open("model.pkl","wb")
pickle.dump(model,f)




