from sklearn import datasets,metrics
#importing gussian naive bayes from slearn
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split

#loading the iris dataset
iris_datasets=datasets.load_iris()

x = iris_datasets.data

#getting the samples and feactures of the dataset.
y = iris_datasets.target

#split the data of arrays or matrices for training and testing cross validation with test size 40%
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=21)

#defining the model
model=GaussianNB()

#fit the training data into model
model.fit(x_train,y_train)

#printing the probability of training data
print(f"The Probability of the traning module is {model.score(x_train,y_train)}")

#testing the 40% of data(test data) which we separated

#define to predict the test data
y_pred = model.predict(x_test)

#calculating the accuracy classification score.
print("The Accuracy score of Naive bayes on test set is : ",metrics.accuracy_score(y_test, y_pred))