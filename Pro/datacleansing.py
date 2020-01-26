# import the pandas library
import pandas as pd
import numpy as np
t=np.random.randn(5, 3)
#print(t)
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
#print(df)

df = df.reindex(['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df.dropna())
