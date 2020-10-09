import numpy as np
from sklearn.preprocessing import MinMaxScaler
demoData = np.random.randint(10, 100, (10 ,2))
demoData
scalar_model = MinMaxScaler()
scalar_model.fit_transform(demoData)

=========================================================================

import numpy as np
from sklearn.preprocessing import MinMaxScaler
demoData = np.random.randint(1, 500, (20 ,4))
demoData

scalar_model = MinMaxScaler()
feature_data = scalar_model.fit_transform(demoData)
feature_data
