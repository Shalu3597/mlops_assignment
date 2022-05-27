# mlops_assignment
Data set: Iris from sklearn <br>
from sklearn.datasets import load_iris <br>
Downloaded the daataset and created data frame <br>
data = load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names)
Performed Exploratory Data Analysis <br>
1. Checking for null
2. Correlation
3. description of the data
