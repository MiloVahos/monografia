import typing as t

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV

def build_estimator(hyperparams: t.Dict[str, t.Any]):
  model = KNeighborsClassifier(hyperparams['n_neighbors'])
  return model
