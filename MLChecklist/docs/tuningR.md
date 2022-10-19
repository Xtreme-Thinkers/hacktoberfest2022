**Now let's tune our Random Forest Regressor and create a final model pipeline 🎈**

```python
# Importing essential libraries
import pandas as pd
import joblib as jb
from sklearn import preprocessing, metrics, impute, model_selection, compose, ensemble

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

# Import the pipeline with scaling excluded because we're using tree based model
cleaning_pipeline_witthout_scaler = jb.load('cleanpipeline2.jb')
```
**Create a list of parameters which is used to tune the random forest regressor**

|Parameters|Description|
|----------|-----------|
|n_estimators|The number of trees in the forest.|
|criterion|The function to measure the quality of a split.|
|max_depth|The maximum depth of the tree. |
|min_samples_split|The minimum number of samples required to split an internal node|
|min_samples_leaf|The minimum number of samples required to be at a leaf node.|
|min_weight_fraction_leaf|The minimum weighted fraction of the sum total of weights (of all the input samples) required to be at a leaf node. |
|max_features|The number of features to consider when looking for the best split:|
|max_leaf_nodes|Grow trees with max_leaf_nodes in best-first fashion. Best nodes are defined as relative reduction in impurity. If None then unlimited number of leaf nodes.|
|min_impurity_decrease|A node will be split if this split induces a decrease of the impurity greater than or equal to this value.|
|bootstrap|Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.|
|oob_score|Whether to use out-of-bag samples to estimate the generalization score.|
|n_jobs|The number of jobs to run in parallel.|
|random_state|Controls both the randomness of the bootstrapping of the samples used when building trees|
|verbose|Controls the verbosity when fitting and predicting.|
|warm_state|When set to True, reuse the solution of the previous call to fit and add more estimators to the ensemble, otherwise, just fit a whole new forest. |
|ccp_alpha|Complexity parameter used for Minimal Cost-Complexity Pruning. |
|max_samples|If bootstrap is True, the number of samples to draw from X to train each base estimator.|

```python
params = {
    'n_estimators' : [int(x) for x in np.linspace(start = 100, stop = 500, num = 5)],
    'max_features' : ['auto', 'sqrt'],
    'max_depth' : [int(x) for x in np.linspace(5, 30, num = 6)],
    'min_samples_split' : [2, 5, 10, 15, 100],
    'min_samples_leaf' : [1, 2, 5, 10]
}

model = ensemble.RandomForestRegressor()
randomizedcv = model_selection.RandomizedSearchCV(model,params)
randomizedcv.fit(cleaning_pipeline_witthout_scaler.fit_transform(x_train),y_train)
```
**Know about best estimator, parameters and score**
```python
# Best parameterized estimator, Optimal parameters, Score achieved after applying optimal parameters 
randomizedcv.best_estimator_, randomizedcv.best_params_, randomizedcv.best_score_
```
**Final Pipeline**
```python
# Transformer used to encode the categorical column
encode = compose.make_column_transformer(
    (preprocessing.OneHotEncoder(drop = 'first',handle_unknown='ignore'),categorical_features),
    remainder = 'passthrough'
)
# Optimal parameterized random forest regressor
model = ensemble.RandomForestRegressor(n_estimators=500,min_samples_split=5,min_samples_leaf=1,max_features='sqrt',max_depth=20)
final_pipeline = pipeline.make_pipeline(encode,model)
final_pipeline.fit(x_train,y_train)
final_pipeline.predict(x_test)
```

**View on [Github](https://github.com/Hg03/Regression)**