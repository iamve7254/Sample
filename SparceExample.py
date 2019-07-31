import pandas as pd
import numpy as np
from pip._vendor.distlib.compat import raw_input

ts = pd.Series(np.random.randn(10))
ts[4:-3]= np.nan
strex=ts.to_sparse()
print(strex)

print(strex.fillna(method='pad'))


# input types
str = raw_input("Enter your input: ")
print ("Received input is : ", str)

str1 = input("Enter your input: ")
print("Received input is : ", str1)

