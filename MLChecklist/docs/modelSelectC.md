**Now let's choose the best machine learning model from wide variety of range 🔅**

```python
# Import essential libraries
import pandas as pd
from sklearn import linear_model, tree, ensemble, svm, neighbors, naive_bayes, neural_network, model_selection,impute,preprocessing,pipeline,compose
from sklearn import metrics
from xgboost import XGBClassifier
import joblib as jb

# Loading the data preprocessing pipeline
cleanIt = jb.load('clean.joblib')

# Read the data
df = pd.read_csv('spaceTrain.csv')

# removing useless columns
features = df.drop(['PassengerId','Cabin','Name','Transported'],axis = 1)
target = df.Transported

# Names of numerical and categorical features
numerical_features = [feat for feat in features if features[feat].dtypes !='O']
categorical_features = [feat for feat in features if feat not in numerical_features]

# Split your dataset into training and testing dataset
x_train,x_test,y_train,y_test = model_selection.train_test_split(features,target,test_size = 0.2,stratify=target)
```

> Now we're creating a model which uses different models and find their accuracy measures in form of dataframe ⚖️⚖️

```python
def compare_models(x_train,x_test,y_train,y_test):
    score_table = {
        'Classifiers': ['Logistic Regression','Stochastic Gradient','Decision Tree','Random Forest','ADABoost','XGBoost','Support Vector','Naive Bayes','MultiLayer Perceptron'],
        'Accuracy Score':[],
        'ROC_AUC':[],
        'F1': []
    }
    models = {'Logreg':linear_model.LogisticRegression(),'sgd':linear_model.SGDClassifier(),'dt':tree.DecisionTreeClassifier(),'rf':ensemble.RandomForestClassifier(),'ada':ensemble.AdaBoostClassifier(),'xgb':XGBClassifier(),'sv':svm.SVC(),'nb':naive_bayes.GaussianNB(),'mlp':neural_network.MLPClassifier()}
    for model in models:
        models[model].fit(x_train.copy(),y_train.copy())
        y_pred = models[model].predict(x_test.copy())
        score_table['Accuracy Score'].append(metrics.accuracy_score(y_test.copy(),y_pred))
        score_table['ROC_AUC'].append(metrics.roc_auc_score(y_test.copy(),y_pred))
        score_table['F1'].append(metrics.f1_score(y_test.copy(),y_pred))
        
    return pd.DataFrame(score_table)

compare_models(cleanIt.fit_transform(x_train),cleanIt.transform(x_test),y_train,y_test)
```

> There are more models to explore, you can simply put in the list of models and make it instance. You're good to go. 

>> ADABoost classifier is giving us great accuracy, roc_auc score and f1 score, so we'll ▶️ with this.

**View on [Github](https://github.com/Hg03/Classification)**