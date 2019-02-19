# import scikit learn datasets libraries
from sklearn import datasets
# import the split function using cross validation
from sklearn.model_selection import train_test_split
# importing the svm model
from sklearn import svm
#  import the metrics for the calculation of accuracy 
from sklearn import metrics

#loads the iris dataset
IRIS = datasets.load_iris()

# create the x and y
X = IRIS.data
y = IRIS.target

#splitting the dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=25)


#creating a svm classifier and kernel is linear
clf = svm.SVC(kernel='linear') 

#model is trained for the training sets
clf.fit(X_train, y_train)

#prediction on test dataset
y_pred = clf.predict(X_test)

# calculating accuracy of test datasets
print("Accuracy of linear svm method is:",metrics.accuracy_score(y_test, y_pred))

#probability of training data
print(f"the probability of training data is:{clf.score(X_train,y_train)}")