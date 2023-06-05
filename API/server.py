from flask import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

raw_data = pd.read_csv('mail_data.csv')

mail_data = raw_data.where((pd.notnull(raw_data)),'')

mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1


X = mail_data['Message']
y = mail_data['Category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(lowercase=True)

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

X_train = feature_extraction.fit_transform(X_train)
X_test = feature_extraction.transform(X_test)

y_train = y_train.astype('int')
y_test = y_test.astype('int')

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_train)

accuracy = accuracy_score(y_train, predictions)

# the main flask code starts here
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/main', methods=['POST'])
def mainApp():
    input_mail = request.form.get('email')

    input_data_features = feature_extraction.transform([input_mail])

    prediction = model.predict(input_data_features)

    if prediction[0] == 1:
        return 'This is unlikely to be a spam mail'
    else:
        return 'This is likely to be a spam mail'

if __name__ == "__main__":
    app.run(debug=True)
    