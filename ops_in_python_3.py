# implementing DVC for data versioning 

import pandas as pd
import os

data = {'name':["akash",'das','kumar'],
        'age':[25,30,16],
        'class':["A",'B','C']}

df = pd.DataFrame(data)

os.makedirs("data",exist_ok=True)

file_path = os.path.join("data","sampleData.csv")

print(file_path)

df.to_csv(file_path,index=False)