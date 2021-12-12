import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rk4s import rk4

def create_df(m, k, c, ks, v1, v2, step, max_steps, control, control_val, limit, limit_acc):
    table = np.array(rk4(m, k, c, ks, v1, v2, step, max_steps, control, control_val, limit, limit_acc))
    df = pd.DataFrame(data=table, columns=['n', 'hn-1', 'xn', 'vn1', 'vn2', 'vn1d', 'vn2d', 'S*', 'повышение', 'понижение'])
    return df

def saveplots(df):
    plt.plot(df['xn'], df['vn1'])
    plt.savefig('vn1.png')
    plt.clf()
    plt.plot(df['xn'], df['vn2'])
    plt.savefig('vn2.png')
    plt.clf()
    plt.plot(df['vn1'], df['vn2'])
    plt.savefig('both.png')
    plt.clf()

def empty_df():
    df = pd.DataFrame(data=None, columns=['n', 'hn-1', 'xn', 'vn1', 'vn2', 'vn1d', 'vn2d', 'S*', 'повышение', 'понижение'])
    return df
# print(df.tail(50))
# plt.plot(df['vn1'], df['vn2'])
# plt.show()
# plt.plot(df['xn'], df['vn2'])
# plt.show()
# plt.plot(df['xn'], df['vn1'])
# plt.show()

df = create_df(5, 2., 0.15, 2., 10., 0., 0.1, 1000, True, 0.0001, 20, 0.001)
print(df)
# saveplots(df)