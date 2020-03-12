import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import pandas as pd



dates = []
number = []

def get_data(filename):
    data = pd.read_csv(filename) 
    for col in data.columns:
        dates.append(int(col.replace('2020-','').replace('-','')))
        number.append(float(data.at[0,col]))
    return

def predict_price(dates, numbers, x):
    dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1

    svr_lin = SVR(kernel= 'linear', C= 1e3)
    svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
    svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
    svr_rbf.fit(dates, numbers) # fitting the data points in the models
    svr_lin.fit(dates, numbers)
    svr_poly.fit(dates, numbers)

    plt.scatter(dates, number, color= 'black', label= 'Data') # plotting the initial datapoints 
    plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
    plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
    plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('data_reform.csv') # calling get_data method by passing the csv file to it
#print "Dates- ", dates
#print "Prices- ", prices

predicted_price = predict_price(dates, number, 50)  