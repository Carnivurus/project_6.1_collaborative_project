'''The following document has the propose to share the different graphics that matplotlib has, 
the data will be generated randomly'''

import pandas as pd
import numpy as np

jp_sales, us_sales = np.random.randint(0, 100, [50, 50])
jp_sales = ', '.join(map(str, jp_sales))
us_sales = ', '.join(map(str, us_sales))

year = np.random.randint(2000, 2016, [50, 50])
game = [f'game_{i}' for i in range(1, 51)]


df = pd.DataFrame(data={
    'game': game,
    'year': year,
    'jp_sales': jp_sales,
    'us_sales': us_sales
})

print(jp_sales)
