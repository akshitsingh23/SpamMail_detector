

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
# from google.colab import files

df = pd.read_csv('./mail_data.csv')
df

data = df.where((pd.notnull(df)),'')

data.head(10)

data.info()

data.shape

data.loc[data['Category']=='spam','Category',]=0
data.loc[data['Category']=='ham','Category',]=1

X = data['Message']
Y = data['Category']

X

Y

X_train, X_test ,Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)

print(X.shape)
print(X_train.shape)
print(X_test.shape)

print(Y.shape)
print(Y_train.shape)
print(Y_test.shape)

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

print(X_train_features)

model = LogisticRegression()

model.fit(X_train_features,Y_train)

prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train,prediction_on_training_data)

print('Acc on training data :', accuracy_on_training_data)

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test,prediction_on_test_data)

print('Acc on training data :', accuracy_on_test_data)

input_mail = ["Win a free car now!"]

input_data_features = feature_extraction.transform(input_mail)

prediction = model.predict(input_data_features)

print(prediction)

if (prediction[0]==1):
  print('Ham mail')
else:
  print('Spam mail')

input_mail = ["FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, Â£1.50 to rcv"]

input_data_features = feature_extraction.transform(input_mail)

prediction = model.predict(input_data_features)
# print(prediction)

if (prediction[0]==1):
  print('Ham mail')

else:
  print('Spam mail')

with open('spam_mail_detector.pkl', 'wb') as file:
    pickle.dump(model, file)

# Download the file
# files.download('spam_mail_detector.pkl')

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(feature_extraction, vectorizer_file)
# files.download('vectorizer.pkl')

import joblib
model = pickle.load(open('spam_mail_detector.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
# vectorizer = pickle.load('./vectorizer.pkl')

data = 'WINNER!! As a valued network customer you have been selected to receivea Â£900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.'
email_vector = vectorizer.transform([data])
email_vector
# Make a prediction
prediction = model.predict(email_vector)
print(prediction)

# Convert the prediction to a human-readable format
result = 'spam' if prediction[0] == 1 else 'Nspam'
print(prediction[0])