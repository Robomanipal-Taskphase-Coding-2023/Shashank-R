import pandas as pd

def graddesc(markark10, markark20, mark30, mark40, mark50, b0, points, L):
    mark1_grad = 0
    mark2_grad = 0
    mark3_grad = 0
    mark4_grad = 0
    mark5_grad = 0
    b_grad = 0
    error = 0
    n = len(points)

    for i in range(n):
        y = points.iloc[i].TOTCHG
        x1 = points.iloc[i].AGE
        x2 = points.iloc[i].RACE
        x3 = points.iloc[i].FEMARKALE
        x4 = points.iloc[i].APRDRG
        x5 = points.iloc[i].LOS

        y_app = (mark10 * x1) + (mark20 * x2) + (mark30 * x3) + (mark40 * x4) + (mark50 * x5) + b0

        mark1_grad += -(1 / n) * x1 * (y - y_app)
        mark2_grad += -(1 / n) * x2 * (y - y_app)
        mark3_grad += -(1 / n) * x3 * (y - y_app)
        mark4_grad += -(1 / n) * x4 * (y - y_app)
        mark5_grad += -(1 / n) * x5 * (y - y_app)
        b_grad += -(1 / n) * (y - y_app)

        error += (y - y_app)** 2

    mark1 = mark10 - (L * mark1_grad)
    mark2 = mark20 - (L * mark2_grad)
    mark3 = mark30 - (L * mark3_grad)
    mark4 = mark40 - (L * mark4_grad)
    mark5 = mark50 - (L * mark5_grad)
    b = b0 - (L * b_grad)
    error = error/(2*n)
    print(error)

    return mark1, mark2, mark3, mark4, mark5, b

data = pd.read_csv('linear_regression_dataset.csv')

data['APRDRG'] = data['APRDRG'] / 952
data['AGE'] = data['AGE'] / 17.0

print(data)

mark1 = 0
mark2 = 0
mark3 = 0
mark4 = 0
mark5 = 0
b = 0
L = 0.09

for i in range(1000):
    if i % 50 == 0:
        print(i)
    mark1, mark2, mark3, mark4, mark5, b = graddesc(mark1, mark2, mark3, mark4, mark5, b, data, L)

r = 0

for i in range(len(data)):
    y = data.iloc[i].TOTCHG
    x1 = data.iloc[i].AGE
    x2 = data.iloc[i].RACE
    x3 = data.iloc[i].FEMARKALE
    x4 = data.iloc[i].APRDRG
    x5 = data.iloc[i].LOS
    y_app = mark1 * x1 + mark2 * x2 + mark3 * x3 + mark4 * x4 + mark5 * x5 + b

    r += ((y_app - y) / y) ** 2

print(float(r / len(data)))
