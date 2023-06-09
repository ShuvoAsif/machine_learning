# pip install requests
# pip install beautifulsoup4 lxml
# [1::1] means start for index1
# python pandas
# python mapplotlib
# scikit-learn
import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[20]]))
