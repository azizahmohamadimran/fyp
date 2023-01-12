from flask import Flask, render_template, request, redirect, url_for, app
from gevent.pywsgi import WSGIServer
from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = Flask(__name__, template_folder="templates")


@app.route('/')
def predictionPage():
    return render_template('predictionPage.html')


@app.route('/result', methods=['POST'])
def result():
    data = pd.read_csv(r'C:\Users\User\Documents\diabetes.csv')

    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.form['n1'])
    val2 = float(request.form['n2'])
    val3 = float(request.form['n3'])
    val4 = float(request.form['n4'])
    val5 = float(request.form['n5'])
    val6 = float(request.form['n6'])
    val7 = float(request.form['n7'])
    val8 = float(request.form['n8'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""
    if pred == [1]:
        result1 = "Positive Diabetes"

    else:
        result1 = "Negative Diabetes"

    return render_template('predictionPage.html', result2=result1)


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
