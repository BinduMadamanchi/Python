from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('College.csv')
keep_col = ['Apps','Accept','Enroll','Top10perc','Top25perc','F.Undergrad','P.Undergrad','Outstate','Room.Board','Books','Personal','PhD','Terminal','S.F.Ratio','perc.alumni','Expend','Grad.Rate']
new_f = dataset[keep_col]
new_f.to_csv("File.csv", index=False)
x = dataset.iloc[:,[1,2,3]]
y = dataset.iloc[:-1]
# see how many samples we have of each species
print(dataset["Apps"].value_counts())

sns.FacetGrid(dataset, hue="Apps", size=10).map(plt.scatter, "Enroll", "Accept")
# do same for petals
sns.FacetGrid(dataset, hue="Apps", size=10).map(plt.scatter, "Top10perc", "Top25perc")
plt.show()
# note that the species are nearly linearly separable with petal size,but sepal sizes are more mixed.
from sklearn import preprocessing

scaler = preprocessing.StandardScaler()

scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

nclusters = 1 # this is the k in kmeans
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)
print(y_cluster_kmeans)