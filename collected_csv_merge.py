# -*- coding: utf-8 -*-
"""Collected_CSV_Merge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zRiJ-j6MyI0GPacJYmESYDqoufS4Vsht
"""

import pandas as pd
import numpy as np
import re
from tqdm import tqdm

n_data = [2401, 299, 581, 595, 706, 758]
ninit_data = n_data[0]
nadd_data = n_data[1:]
init_path = f"data_{ninit_data}.csv"

def refineTitle(title):
  text = title
  text = text.strip()

  return text

data = pd.read_csv(init_path, index_col=0)
print("init = ", init_path)
for n in nadd_data:
  add_path = f"data_{n}.csv"
  print("length : ", len(data))
  print("Add : ", add_path)
  add_data = pd.read_csv(add_path, index_col=0)
  data = data.append(add_data,ignore_index=True)

data['Name'] = data['Name'].apply(refineTitle)
data.drop_duplicates(['Name'],inplace=True)

data_len = len(data)
print("length : ", len(data))
data.to_csv(f"collection_{data_len}.csv", index=False)

print("Complete!")