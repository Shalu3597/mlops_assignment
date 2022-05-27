# mlops_assignment
Data set: Iris from sklearn <br>
from sklearn.datasets import load_iris <br>
Downloaded the daataset and created data frame <br>
data = load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names) <br>
Performed Exploratory Data Analysis <br>
1. Checking for null
2. Correlation
3. Description of the data <br>
Splitted train and test data <br>
70% training and 30% test <br>
Performed Logistic Regression and Decision tree classifier and calculated accuracy score for each model. <br>
# Data Drift:
Taken train and test data, considering test data as a new dataset performed statistics on these two data's using tensorflow data validation. <br>
Library to install: <br>
!pip install tensorflow_data_validation
Performed chi2test on these data and the result of P-value is 1 and stat is 197.725. <br>
Since P- value < 0.05 rejected null hypothesis. There is no drift in the data. <br>
# Pickle file
Created pickle file and saved it in the classifier.pkl <br>
Created requirement.txt 
# Deployment
Deployed the machine learning model using Flask. <br>
Read the pickle file. <br>
Imported flasgger. <br>
GET Method used to get the input of 4 featues and predictions done. <br>
Getting the test file data. <br>
Implemented drift in flask.<br>
# Creating container in Docker
Created dockerfile.txt and from anaconds copied the appropriate folder and run python code<br>
Created requirements.txt <br>
Creating container:<br> docker build -t application_1 -f Dockerfile.txt . <br>
Running the application:<br> docker run -p 8000:8000 application_1 <br>

