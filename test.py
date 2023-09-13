import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = sns.load_dataset('titanic')

group = df.groupby(['sex'])
df1 = pd.DataFrame(df)
df1 = df.groupby(['sex'])


print(df1)


