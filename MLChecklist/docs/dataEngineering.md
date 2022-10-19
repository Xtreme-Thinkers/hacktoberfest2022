**As we know, we don't have missing values, therefore we'll perform following steps**

1️⃣ Encoding the categorical features
2️⃣ Scaling the numerical features

```python
# Importing essential libraries
import pandas as pd
from sklearn import preprocessing, impute, model_selection, compose

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

**Let's look at the number of categories in each feature**
```python
no_of_categories = 0
for i in categorical_features:
    no_of_categories = no_of_categories + len(features[i].unique())
print(f'Number of categories in every feature are {no_of_categories} \n')
print(f'Numbe of categories we got after encoding are {no_of_categories - len(categorical_features)} \n')
print('-----------------------------------------------------------------------\n')

for i in categorical_features:
    print(f'Number of categories in "{i}" named column are :- {len(features[i].unique())} \n')
```
 
**Create a pipeline for data transformation**
```python
transform = compose.make_column_transformer(
    (preprocessing.StandardScaler(),numerical_features),
    (preprocessing.OneHotEncoder(drop = 'first',handle_unknown='ignore'),categorical_features),
    remainder='passthrough'
)
```

**There is a catch here, if we are using any tree based model (decision tree, random forest etc), there is no need to scale the columns. Create another pipeline with scaler**
```python
tree_transform = compose.make_column_transformer(
    (preprocessing.OneHotEncoder(drop = 'first',handle_unknown='ignore'),categorical_features),
    remainder = 'passthrough'
)
```

**Save the pipelines**
```python
import joblib as jb
jb.dump(transform,'cleanpipeline1.jb')
jb.dump(tree_transform,'cleanpipeline2.jb')
```

**View on [Github](https://github.com/Hg03/Regression)**