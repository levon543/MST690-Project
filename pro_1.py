import seaborn as sn
import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv (r'C:\FILEPATH\FILE.csv')

df = pd.DataFrame(data)

corrMatrix = df.corr()

print (corrMatrix)

sn.heatmap(corrMatrix, annot=True)
plt.show()    
