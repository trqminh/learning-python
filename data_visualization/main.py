import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # visualization tool

from subprocess import check_output
print(check_output(["ls", "./input"]).decode("utf8"))

data = pd.read_csv("./input/pokemon.csv")

print(data.info())

print(data.corr())

# f, ax = plt.subplots(figsize=(18, 18))
# sns.heatmap(data.corr(), annot=True, linewidths=.5,fmt='.1f', ax=ax)
# plt.show()

print(data.head(10))


