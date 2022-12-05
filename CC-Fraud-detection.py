import pandas as pd
import numpy as np


# Load the csv file
data = pd.read_csv(r'D:\cc.csv',sep=";", encoding='cp1252')
print(data)

#removing null values
s=data.isnull().values.any()
#print(s)
#So  o null values are present in our data

# we have interest in limit of cc


non_fraud = len(data[data.Class == 0])
fraud = len(data[data.Class == 1])
fraud_percent = (fraud / (fraud + non_fraud)) * 100

print("Number of Genuine transactions: ", non_fraud)
print("Number of Fraud transactions: ", fraud)
print("Percentage of Fraud transactions: {:.4f}".format(fraud_percent))

import matplotlib.pyplot as plt
labels = ["Genuine", "Fraud"]
count_classes = data.value_counts(data['Credit Limit'], sort= True)
count_classes.plot(kind = "bar", rot = 0)
plt.title("Visualization of Labels")
plt.ylabel("Count")
plt.xticks(range(2), labels)
plt.show()