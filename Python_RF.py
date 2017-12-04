# sudo apt-get install python-("NumPy", "SciPy", "sklearn", "matplotlib")) modules 

# Load the library with the iris dataset
from sklearn.datasets import load_iris

# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier

# Load pandas
import pandas as pd

# Load numpy
import numpy as np

# Set random seed
np.random.seed(0)

# Create an object called iris with the iris data
iris = load_iris()

# Create a dataframe with the four feature variables
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# View the top 5 rows
# en la terminal -> df.head()

# Add a new column with the species names, this is what we are going to try to predict
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# View the top 5 rows
# en la terminal -> df.head()

# Create a new column that for each row, generates a random number between 0 and 1, and
# if that value is less than or equal to .75, then sets the value of that cell as True
# and false otherwise. This is a quick and dirty way of randomly assigning some rows to
# be used as the training data and some as the test data.
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

# View the top 5 rows
# en la terminal -> df.head()

# Create two new dataframes, one with the training rows, one with the test rows
train, test = df[df['is_train']==True], df[df['is_train']==False]

# Show the number of observations for the test and training dataframes
#print('Number of observations in the training data:', len(train))
#print('Number of observations in the test data:',len(test))

#Procesos de datos

# Create a list of the feature column's names
features = df.columns[:4]

#en la terminal -> features

# train['species'] contains the actual species names. Before we can use it,
# we need to convert each species name into a digit. So, in this case there
# are three species, which have been coded as 0, 1, or 2.
y = pd.factorize(train['species'])[0]

# View target
# en la terminal -> y

#Entrenamiento para Random Forest Classifier

# Create a random forest Classifier. By convention, clf means 'Classifier'
clf = RandomForestClassifier(n_jobs=2, random_state=0)

# Train the Classifier to take the training features and learn how they relate
# to the training y (the species)

x = clf.fit(train[features], y)

# Huzzah! We have done it! We have officially trained our random forest Classifier!
# Now let's play with it. The Classifier model itself is stored in the clf variable.

#Aplicando Clasidicador a un test de datos...

# en la terminal -> x.predict(test[features]) entrega un arreglo

#array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2,
#       2, 2, 2, 2, 2, 2, 2, 2, 2])

# View the predicted probabilities of the first 10 observations
# en al terminal -> x.predict_proba(test[features])[0:10]

#Evaluando el clasificador 

# Create actual english names for the plants for each predicted plant class
preds = iris.target_names[clf.predict(test[features])]

# View the PREDICTED species for the first five observations
# en al terminal -> preds[0:5]

# View the ACTUAL species for the first five observations
# en al terminal -> test['species'].head()


# Create confusion matrix
# terminal-> pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species'])

# View a list of the features and their importance scores
# en el terminal -> list(zip(train[features], clf.feature_importances_))

