from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
import pandas as pd
import joblib

data = fetch_california_housing()

# features(input) and labels(output)
X = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target

print(f'total records:{X.shape[0]}')

# splitting the data for training and testing
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# training a model
model = RandomForestRegressor(
  n_estimators=100, #crete 100 trees
  random_state=42
)
model.fit(X_train,y_train) 

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred) #gives the output b/t 0 and 1


print(f"avg error: ${mae*100000:,.0f}")

# dump the model in joblib
joblib.dump(model,'house_model.joblib')
joblib.dump(list(X.columns),"house_features.joblib")