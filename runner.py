import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rk4s import rk4

table = np.array(rk4(1, 2., 0.15, 2., 10., 0., 0.1, True, False, 0., 1000))
df = pd.DataFrame(data=table, columns=['n', 'hn-1', 'xn', 'vn1', 'vn2', 'vn1d', 'vn2d'])
print(df.head(50))
plt.plot(df['xn'], df['vn1'])
plt.show()