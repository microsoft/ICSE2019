# data loading and splitting scripts
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd

def save_wine_as_csv(np_X, np_y, file_name):
	"""
	Save various splits of the sklearn wine dataset
	"""

	columns = [ 'Alcohol',
	'Malic acid',
	'Ash',
	'Alcalinity of ash',
	'Magnesium',
	'Total phenols',
	'Flavanoids',
	'Nonflavanoid phenols',
	'Proanthocyanins',
	'Color intensity',
	'Hue',
	'OD280/OD315 of diluted wines',
	'Proline',
	'class']


	X = pd.DataFrame(np_X)
	X['class'] = np_y
	X.columns = columns

	X.to_csv(file_name, index=False)

	

X_np, y_np = load_wine(return_X_y=True)
save_wine_as_csv(X_np, y_np, 'wine.csv')

# random state that is not so random
X_train, X_test, y_train, y_test = \
	train_test_split(X_np, y_np, test_size=0.20, random_state=42)

save_wine_as_csv(X_train, y_train, 'wine_train.csv')
save_wine_as_csv(X_test, y_test, 'wine_test.csv')



