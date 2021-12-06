import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rk4s import rk4

table = np.array(rk4(1, 2., 0.15, 2., 10., 0., 0.01, True, True, 0.0001, 10000))
df = pd.DataFrame(data=table, columns=['n', 'hn-1', 'xn', 'vn1', 'vn2', 'vn1d', 'vn2d', 'S*'])
print(df.tail(50))
plt.plot(df['vn1'], df['vn2'])
plt.show()
plt.plot(df['xn'], df['vn2'])
plt.show()
plt.plot(df['xn'], df['vn1'])
plt.show()