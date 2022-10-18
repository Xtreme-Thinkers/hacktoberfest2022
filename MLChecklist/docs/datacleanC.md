## Data Cleaning 🧹

**Let's clean data as we explored before**

> ## Steps to clean data

> 1️⃣ Remove useless columns like Cabin,Name,PassengerId

> 2️⃣ Splitting the dataset (or cross validation)

> 3️⃣ Handling missing values in numerical and categorical features (replacing or removing)

> 4️⃣ Handling outliers (replacing or removing)

> 5️⃣ Handling categorical features (encoding)

> 6️⃣ Feature extraction (We're skipping it, because we've already less columns)

> 7️⃣ Pipeline generation

```python
#Importing essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn import impute, preprocessing, pipeline, model_selection, compose
import joblib

# Reading the data
df = pd.read_csv('spaceTrain.csv')

# removing useless columns and separating independent and independent variables
features = df.drop(['PassengerId','Cabin','Name','Transported'],axis = 1)
target = df.Transported

# Names of numerical features
numerical_features = [feat for feat in features if features[feat].dtypes !='O']

# Names of categorical features
categorical_features = [feat for feat in features if feat not in numerical_features]
```
> Before doing any cleaning/preprocessing, split the dataset into training and testing data

```python
# Split your dataset into training and testing dataset
x_train,x_test,y_train,y_test = model_selection.train_test_split(features,target,test_size = 0.2,stratify=target)
```
> You can check the length of training and testing data to verify ,it si splitted or not.

```python
len(x_train),len(x_test),len(y_train),len(y_test)
```
### Handle missing values in numerical features and categorical features

**We have to impute missing values such that each columns kernel distribution becomes gaussian i.e. bell curve**

```python
plt.figure(figsize=(10,10))
j=1
for i in numerical_features:
    plt.subplot(3,2,j)
    sns.kdeplot(data = df,x=i)
    j+=1
```
> Distribution is not normal/Gaussian but near to normal

```python
# Create instance of each type of imputer available in sklearn library
mean_impute = impute.SimpleImputer(strategy='mean')
median_impute = impute.SimpleImputer(strategy='median')
iterative_impute = impute.IterativeImputer(random_state = 30)
knn_impute = impute.KNNImputer(n_neighbors=3)

#Transform the data with correspondent transformers
with_mean = mean_impute.fit_transform(x_train[numerical_features])
with_median = median_impute.fit_transform(x_train[numerical_features])
with_iterative = iterative_impute.fit_transform(x_train[numerical_features])
with_knn = knn_impute.fit_transform(x_train[numerical_features])

# Visualize the columns after imputing with mean
plt.figure(figsize=(10,10))
j=1
for i in pd.DataFrame(with_mean).columns:
    plt.subplot(3,2,j)
    sns.kdeplot(x=with_mean[i])
    j+=1
```

> We can visualize other columns distribution using above code of other imputations

#### On observing each distribution on each imputation, we can see all distributions are same , so we can choose any imputation technique. For e.g. let's choose mean imputation

```python
# Now let's impute categorical features

# Create instance of imputation
mode_impute = impute.SimpleImputer(strategy='most_frequent')
const_impute = impute.SimpleImputer(strategy='constant',fill_value='not_specified')

# As we know HomePlanet and Destination are colums which we are imputing with constant value like 'not_specified' and CryoSleep and VIP with their mode value.
for_mode_feat = ['CryoSleep','VIP'] 
for_constant_feat = ['HomePlanet','Destination']
with_mode = mode_impute.fit_transform(x_train[for_mode_feat])
with_const = const_impute.fit_transform(x_train[for_constant_feat])

# We can confirm that values are imputed
pd.DataFrame(with_mode).isnull().sum().sum(),pd.DataFrame(with_const).isnull().sum().sum()
```

### Now let's encode the categorical columns
**Keeping in mind that ordinal and nominal specificness**

> Ordinal features are those categorical features which has values comparable
>> We have two features which are **VIP** and **CryoSleep**

> Nominal features are those categorical features which has values uncomparable
>> We have two features which are **HomePlanet** and **Destination**

```python
# Create instances for ordinal and one hot encoder
ordinal_encoder = preprocessing.OrdinalEncoder()
onehot_encoder = preprocessing.OneHotEncoder(drop='first')

# Fit the data in encoders
with_ordinal = ordinal_encoder.fit_transform(with_mode)
with_onehot = onehot_encoder.fit_transform(with_const)
```
> We've encoded the categorical columns successfully

### Now let's deal with outliers

```python
def CustomSampler_IQR (X, y):
    
    features = X.columns
    df = X.copy()
    df['Transported'] = y
    
    indices = [x for x in df.index]    
    out_indexlist = []
    for col in features:
        upper_indices = []
        lower_indices = []
        #Using nanpercentile instead of percentile because of nan values
        Q1 = np.nanpercentile(df[col], 25.)
        Q3 = np.nanpercentile(df[col], 75.)
        
        cut_off = (Q3 - Q1) * 1.5
        upper, lower = Q3 + cut_off, Q1 - cut_off
                
        upper_indices = df[col][df[col] < lower].index.tolist()
        lower_indices = df[col][df[col] > upper].index.tolist()
        X.loc[upper_indices][col] = upper
        X.loc[lower_indices][col] = lower
        #outliers = df[col][(df[col] < lower) | (df[col] > upper)].values        
        #out_indexlist.extend(outliers_index)
        
        
    #using set to remove duplicates
    #out_indexlist = list(set(out_indexlist))
    
    #clean_data = np.setdiff1d(indices,out_indexlist)

    return X, y

dfa = pd.DataFrame(with_mean,columns=numerical_features).reset_index(drop=True) # with_mean has no column names, therefore we've fixed it and reset the indices
clean_x,clean_y = CustomSampler_IQR(dfa,y_train.reset_index(drop=True))
```
> * If you want to remove or replace outliers, this function helps greatly, above function is replacing the outliers with upper and lower value,
> * Commented code will helps to remove the outliers. Just pass the independent features data, function will deals with outlier in each numerical columns.

**There is a catch is removing outliers, because if there is so much row which have outlying values, we can remove because it results to loss of data**

**It's upto you, you can use it or not !!**

### Now let's create a pipeline for data preprocessing

```python
# Column transformer transform columns parallely, so make you pass different columns on every transformer inside it.

# Imputing Transformer
imputer = compose.make_column_transformer(
    (impute.SimpleImputer(strategy='mean'),[3,5,6,7,8,9]),
    (impute.SimpleImputer(strategy='most_frequent'),[1,4]),
    (impute.SimpleImputer(strategy='constant',fill_value='not_specified'),[0,2]),
    remainder='passthrough'
)

# Categorical Transformer
encoding = compose.make_column_transformer(
    (preprocessing.OrdinalEncoder(),[6,7]),
    (preprocessing.OneHotEncoder(drop='first'),[8,9]),
    remainder='passthrough'
)

# Pipeline executes the transformer (or group of) sequentially
cleaning_pipeline = pipeline.make_pipeline(imputer,encoding)
```
> * As we can see above, columns are passed in terms of numbered position because, on applying transformer, our data will loose its column names therefore provide columns through numbers.
> * As we are passing whole data, columns which are transforming first placed at beginning automatically.

### Save the pipeline if required

```python
# Saving the pipeline
joblib.dump(cleaning_pipeline,'clean.joblib')

# Loading the saved pipeline
clean_pipe = joblib.load('clean.joblib') # use 'clean_pipe same as we use pipeline'
``` 

**Note **- Don't worry about losing the column names on applying transformer, sklearn will handle all this.

**View on [Github](https://github.com/Hg03/Classification)**



