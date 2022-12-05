#import pandas as pd
#data=pd.read_csv(r"D:\Project survey.csv")


import pandas as pd
from scipy.stats import chisquare
data = pd.read_csv("D:\CarBrands.csv")
print(data)

print(data.describe())




