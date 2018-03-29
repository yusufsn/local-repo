import pandas as pd
import os, csv
import numpy as np

userhome = os.path.expanduser('~')
filename = userhome + r'/local-repo/script/data.csv' 
data = pd.DataFrame(np.random.randint(low=0, high=10, size=(20,5)),
					columns=['a', 'b', 'c', 'd', 'e'])

print('data frame :')
print(data)

#write into csv
data.to_csv(filename)

#drop duplicate data
dd = data.drop_duplicates(['d', 'e'])
print('Drop duplicate data based on column d and e:')
print(dd)