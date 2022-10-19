**Let's choose the model from different type of regresion models 🔅**

> Import the libraries, read the data and previous discussed stuff

```python
# Importing essential libraries
import pandas as pd
import joblib as jb
from sklearn import preprocessing, metrics, impute, model_selection, compose, linear_model, tree, svm, ensemble

# Reading data
df = pd.read_csv('data.csv')
df.drop('car_ID',axis=1,inplace=True)
# Split in feature and target for future purpose
features = df.drop(['CarName','price'],axis=1)
target = df.price

# Names of numerical and categorical features
numerical_features = [col for col in features.columns if features[col].dtypes!='O']
categorical_features = [col for col in features.columns if col not in numerical_features]

# Train test split
x_train,x_test,y_train,y_test = model_selection.train_test_split(features,target,random_state=32)

# Nominal features
nominal_features = ['fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','enginetype','cylindernumber','fuelsystem']
```

**Load the data transformation pipeline we've created in previous slides**
```python
cleaning_pipeline_with_scaler = jb.load('cleanpipeline1.jb')
cleaning_pipeline_witthout_scaler = jb.load('cleanpipeline2.jb')
```
**Now we're using that same function we've discussed in [classification section 🔗](/modelSelectC)**

```python
# With scaling included
def compare_models_notree(x_train,x_test,y_train,y_test):
    score_table = {
        'Classifiers': ['Linear Regression','Ridge Regression','Lasso Regression','Support Vector Regression','Huber Regression'],
        'r_square':[],
        'mae':[],
        'mse': []
    }
    models = {'Linreg':linear_model.LinearRegression(),'ridge':linear_model.Ridge(),'lasso':linear_model.Lasso(),'svr':svm.SVR(),'huber':linear_model.HuberRegressor()}
    for model in models:
        models[model].fit(x_train.copy(),y_train.copy())
        y_pred = models[model].predict(x_test.copy())
        score_table['r_square'].append(metrics.r2_score(y_test.copy(),y_pred))
        score_table['mae'].append(metrics.mean_absolute_error(y_test.copy(),y_pred))
        score_table['mse'].append(metrics.mean_squared_error(y_test.copy(),y_pred))
        
    return pd.DataFrame(score_table)

compare_models_notree(cleaning_pipeline_with_scaler.fit_transform(x_train),cleaning_pipeline_with_scaler.transform(x_test),y_train,y_test)
```

```python
# With scaling excluded
def compare_models_tree(x_train,x_test,y_train,y_test):
    score_table = {
        'Classifiers': ['Decision Tree','Random Forest','ADABoost'],
        'r_square':[],
        'mae':[],
        'mse': []
    }
    models = {'dt':tree.DecisionTreeRegressor(),'rf':ensemble.RandomForestRegressor(),'ada':ensemble.AdaBoostRegressor()}
    for model in models:
        models[model].fit(x_train.copy(),y_train.copy())
        y_pred = models[model].predict(x_test.copy())
        score_table['r_square'].append(metrics.r2_score(y_test.copy(),y_pred))
        score_table['mae'].append(metrics.mean_absolute_error(y_test.copy(),y_pred))
        score_table['mse'].append(metrics.mean_squared_error(y_test.copy(),y_pred))
        
    return pd.DataFrame(score_table)

compare_models_tree(cleaning_pipeline_with_scaler.fit_transform(x_train),cleaning_pipeline_with_scaler.transform(x_test),y_train,y_test)
```

> Boooom , tree regressor is winning by the way i.e. Random Forest Regression

**View on [Github](https://github.com/Hg03/Regression)**
