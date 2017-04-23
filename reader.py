import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
import sys

df = pd.read_csv('../test_data/baseballdatabank-2017.1/core/Salaries.csv')

current = df.loc[df['yearID'] >= 2016]

print(current)