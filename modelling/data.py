
import typing as t
import typing_extensions as te

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor

class DatasetReader(te.Protocol):
  def __call__(self) -> pd.DataFrame:
    ... # What does this mean?

SplitName = te.Literal["train", "test"]

def get_dataset(reader: DatasetReader, splits: t.Iterable[SplitName]):
  df = reader()
  df = clean_dataset(df)
  y = df["diagnosis"]
  X = df.drop(columns=["diagnosis", "id"])
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.3, random_state=1
  )
  split_mapping = {"train": (X_train, y_train), "test": (X_test, y_test)}
  return {k: split_mapping[k] for k in splits}

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
  df_breast_cancer_numbers = df.drop(columns = ['diagnosis', 'id'])
  LOF = LocalOutlierFactor(n_neighbors = 5, algorithm = 'auto', metric = 'euclidean')
  Filtrado = LOF.fit_predict(df_breast_cancer_numbers)
  NOF = LOF.negative_outlier_factor_
  ground_truth = np.ones(len(df_breast_cancer_numbers), dtype = int)
  pos = np.where(Filtrado == ground_truth)
  pos = np.asarray(pos)
  pos = np.hstack(pos)
  df_breast_cancer_LOF = df.loc[pos, :]
  return df_breast_cancer_LOF